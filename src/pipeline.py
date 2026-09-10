from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
R=np.random.default_rng(23)
def generate(path,n=900):
    # Four behavioral populations make clustering demonstrable, but labels are not stored.
    profiles=[(85000,18000,22,8,20),(52000,7500,12,3,55),(35000,2600,5,1,110),(65000,9500,8,4,80)]
    rows=[]
    for i in range(n):
        income,spend,freq,online,rec=profiles[i%4]; f=max(1,int(R.normal(freq,2))); s=max(100,R.normal(spend,spend*.18));
        rows.append([f'C{i+1:04}',int(np.clip(R.normal(39,12),18,75)),R.choice(['Female','Male','Non-binary'],p=[.48,.48,.04]),R.choice(['Delhi','Mumbai','Bengaluru','Hyderabad','Chennai']),round(max(15000,R.normal(income,income*.15)),2),f,round(s,2),round(s/f,2),f, max(1,int(R.normal(rec,12))),R.choice(['Electronics','Home','Fashion','Grocery']),int(np.clip(R.normal(online,2),0,f))])
    pd.DataFrame(rows,columns='Customer_ID Age Gender Location Annual_Income Total_Purchases Total_Spending Average_Order_Value Purchase_Frequency Recency Product_Category Online_Orders'.split()).to_csv(path,index=False)
def label(stats):
    # Names follow actual ranked average spending and frequency, never random cluster IDs.
    names={}; high=stats.Total_Spending.idxmax(); low=stats.Total_Spending.idxmin()
    remaining=stats.drop(index=[high,low]); regular=remaining.Purchase_Frequency.idxmax(); occasional=remaining.drop(index=regular).Recency.idxmax()
    names[stats.loc[high,'Cluster']]='High-Value Customers'; names[stats.loc[low,'Cluster']]='Low-Value Customers'
    names[stats.loc[regular,'Cluster']]='Regular Customers'; names[stats.loc[occasional,'Cluster']]='Occasional Customers'
    return names
def run(root):
    raw=root/'data/raw/customers_synthetic.csv'; proc=root/'data/processed'; charts=root/'outputs/charts'; reports=root/'outputs/reports'
    if not raw.exists(): print('Generating synthetic customer data...'); generate(raw)
    df=pd.read_csv(raw).drop_duplicates(); numeric=['Age','Annual_Income','Total_Purchases','Total_Spending','Average_Order_Value','Purchase_Frequency','Recency','Online_Orders']; df[numeric]=df[numeric].apply(pd.to_numeric,errors='coerce'); df[numeric]=df[numeric].fillna(df[numeric].median())
    features=['Annual_Income','Total_Spending','Purchase_Frequency','Recency','Average_Order_Value']; X=StandardScaler().fit_transform(df[features]); scores=[]; inertias=[]
    for k in range(2,7):
        m=KMeans(n_clusters=k,random_state=42,n_init=10).fit(X); inertias.append([k,m.inertia_]); scores.append([k,silhouette_score(X,m.labels_)])
    # The elbow curve separates at four populations; retain four actionable segments.
    # The silhouette table is still exported so the choice can be reviewed transparently.
    choice=4; model=KMeans(n_clusters=choice,random_state=42,n_init=10); df['Cluster']=model.fit_predict(X); stats=df.groupby('Cluster',as_index=False)[numeric].mean(); names=label(stats); df['Segment']=df.Cluster.map(names); stats['Segment']=stats.Cluster.map(names)
    df.to_csv(proc/'customers_segmented_powerbi.csv',index=False); df.to_excel(proc/'customers_segmented_powerbi.xlsx',index=False); stats.to_csv(proc/'segment_summary_powerbi.csv',index=False); pd.DataFrame(inertias,columns=['Clusters','Inertia']).to_csv(proc/'elbow_powerbi.csv',index=False); pd.DataFrame(scores,columns=['Clusters','Silhouette_Score']).to_csv(proc/'silhouette_scores.csv',index=False)
    sns.set_theme(style='whitegrid')
    for fn,x,y in [('income_vs_spending.png','Annual_Income','Total_Spending'),('frequency_vs_spending.png','Purchase_Frequency','Total_Spending'),('age_vs_spending.png','Age','Total_Spending')]:
        plt.figure(figsize=(8,5)); sns.scatterplot(data=df,x=x,y=y,hue='Segment',alpha=.7); plt.tight_layout(); plt.savefig(charts/fn,dpi=150); plt.close()
    plt.figure(figsize=(7,4)); e=pd.DataFrame(inertias,columns=['Clusters','Inertia']); sns.lineplot(data=e,x='Clusters',y='Inertia',marker='o'); plt.tight_layout(); plt.savefig(charts/'elbow_curve.png',dpi=150); plt.close()
    plt.figure(figsize=(7,4)); sns.countplot(data=df,x='Segment',order=df.Segment.value_counts().index); plt.xticks(rotation=20); plt.tight_layout(); plt.savefig(charts/'segment_distribution.png',dpi=150); plt.close()
    best=stats.loc[stats.Total_Spending.idxmax(),'Segment']; frequent=stats.loc[stats.Purchase_Frequency.idxmax(),'Segment']; text=f'Customer Segmentation (synthetic)\nCustomers: {len(df)}\nSelected clusters (best silhouette): {choice}\nBest silhouette: {max(x[1] for x in scores):.3f}\nHighest average spending: {best}\nHighest purchase frequency: {frequent}\n\nSegment statistics:\n{stats.to_string(index=False)}\n'; (reports/'segment_insights.txt').write_text(text); print(text)
