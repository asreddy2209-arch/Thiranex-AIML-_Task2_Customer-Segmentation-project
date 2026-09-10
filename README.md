# Customer Segmentation Using Machine Learning

Run `python main.py`. Synthetic customer data is placed in `data/raw/`; the K-Means output, segment summary, elbow and silhouette tables are in `data/processed/`. Segment names are assigned from measured spending, frequency, and recency characteristics, rather than K-Means IDs.

## Power BI
Import `customers_segmented_powerbi.csv` and `segment_summary_powerbi.csv`. Add cards for customer count, average spending, average income and purchase frequency. Use Segment distribution, Segment/Total_Spending, Gender, and Location visuals, with Segment, Gender, and Location slicers. The included scatter charts document the EDA.

Target high-spending segments with retention benefits; use the lower-spending or occasional segments for tailored reactivation offers. Exact current results are in `outputs/reports/segment_insights.txt`.
