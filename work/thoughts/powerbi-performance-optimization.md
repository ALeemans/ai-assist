---
type: thought
category: work
created: 2026-01-30
tags: [power-bi, performance, optimization, transform-data, query-folding]
related_to: User Story #145886
---

# Power BI Performance Optimization Ideas

## Problem
Domain teams experience extremely long loading times in Power BI Transform Data (Power Query Editor). This severely impacts productivity and makes data modeling inefficient.

## Root Cause Analysis - Possible Issues

### 1. Query Folding Not Happening
- Power Query steps may not be "folding" to the data source
- Complex M code transformations force local processing
- **Check**: Review each query step - yellow/white background indicates folding status
- **Solution**: Restructure queries to push operations to source database

### 2. Large Data Volumes in Preview
- Transform Data loads full dataset for preview
- Millions of rows = slow performance
- **Check**: Review row counts in queries
- **Solution**: 
  - Use `Table.FirstN()` for development/testing
  - Implement data source filters (WHERE clauses)
  - Consider incremental refresh

### 3. Too Many Queries/Dependencies
- Excessive number of queries
- Circular or complex dependencies
- Each query refresh cascades
- **Check**: Query Dependencies view
- **Solution**: Consolidate queries, remove unused queries

### 4. Inefficient M Code
- Nested `Table.AddColumn` operations
- Multiple merge operations
- Poor use of buffering
- **Check**: Review M code in Advanced Editor
- **Solution**: Rewrite using efficient patterns, use `Table.TransformColumns` instead of repeated AddColumn

### 5. Data Source Performance
- Slow SQL Server queries
- Missing indexes on source tables
- Network latency
- **Check**: Run source queries directly in SQL Server
- **Solution**: Add indexes, optimize SQL views, use stored procedures

### 6. Privacy Levels Causing Issues
- Privacy level settings forcing data combination in Power Query
- **Check**: Privacy Level settings in Data Source Settings
- **Solution**: Set appropriate privacy levels, use "Ignore Privacy Levels" if safe

## Optimization Strategies

### Short-term Quick Wins
1. **Disable Auto Detect Relationships** during development
   - File > Options > Current File > Data Load
   - Uncheck "Autodetect new relationships"

2. **Reduce Query Preview Rows**
   - Options > Data Load > Default Query Load Settings
   - Set lower row count for preview

3. **Disable Background Data Refresh** during editing
   - Options > Data Load
   - Uncheck "Allow data preview to download in the background"

4. **Remove Unused Queries**
   - Delete or disable loading for reference queries
   - Right-click query > Enable Load (uncheck)

### Medium-term Improvements
1. **Implement Query Folding Best Practices**
   - Use native SQL queries where possible
   - Push filtering to source
   - Avoid custom columns that break folding
   - Use View Source to verify what SQL is generated

2. **Optimize Merge/Join Operations**
   - Ensure merge columns are indexed in source
   - Use appropriate join types (inner vs left)
   - Consider doing joins in SQL source instead

3. **Use Parameters for Development**
   - Create parameter for row limit
   - Add `Table.FirstN(Source, RowLimit)` at start
   - Set to 1000 during dev, NULL for production

4. **Implement Incremental Refresh**
   - For large fact tables
   - Only refresh recent data
   - Archive historical data

### Long-term Solutions
1. **Dataflow Architecture**
   - Move common transformations to Power BI Dataflows
   - Reuse across multiple datasets
   - Centralize heavy processing

2. **Data Warehouse Layer**
   - Pre-aggregate data in SQL
   - Create optimized views/tables
   - Implement SCD (Slowly Changing Dimensions) in warehouse

3. **DirectQuery vs Import Evaluation**
   - Consider DirectQuery for real-time scenarios
   - Hybrid models (Import + DirectQuery)
   - Aggregations table strategy

4. **Optimize Data Model**
   - Star schema design
   - Remove unnecessary columns
   - Optimize data types (use Integer instead of Text where possible)
   - Implement calculated columns vs measures appropriately

## Diagnostic Steps

### Step 1: Measure Current Performance
- Document current load times per query
- Identify slowest queries
- Check Query Diagnostics tool

### Step 2: Enable Query Diagnostics
- Tools > Query Diagnostics > Start Diagnostics
- Refresh queries
- Analyze diagnostic results
- Look for bottlenecks

### Step 3: Review Data Source
- Check source database performance
- Review execution plans for source queries
- Identify missing indexes
- Check network latency

### Step 4: Analyze M Code
- Review each query's M code
- Look for anti-patterns
- Check if query folding is occurring
- Identify unnecessary transformations

## Specific Recommendations for HU Data Analytics

### For Domain Team Models
1. **Create Template with Optimized Settings**
   - Pre-configured with best practice settings
   - Include parameter for row limits
   - Document optimization guidelines

2. **Standardize Data Source Queries**
   - Create centralized SQL views
   - Ensure proper indexing
   - Use stored procedures for complex logic

3. **Training & Documentation**
   - Train domain teams on query folding
   - Document performance best practices
   - Create Power BI optimization checklist

4. **Regular Performance Reviews**
   - Monthly check of slowest models
   - Identify common anti-patterns
   - Share optimization wins across teams

### For Transform Data Specifically
1. **Reduce Auto-Refresh Frequency**
   - Don't refresh all queries on every change
   - Use "Refresh Preview" selectively
   - Work with data preview disabled when possible

2. **Separate Development/Production**
   - Use small sample datasets during development
   - Switch to full dataset only for final testing
   - Parameter-based approach

3. **Profile Only When Needed**
   - Column profiling is expensive
   - Disable by default
   - Enable only when analyzing data quality

## Testing Plan
1. Implement one optimization at a time
2. Measure before/after performance
3. Document what works
4. Share findings with domain teams
5. Create best practices guide

## Success Metrics
- Load time in Transform Data < 10 seconds (target)
- Query refresh time reduced by 50%+
- Domain team satisfaction improved
- Number of performance complaints reduced

## Resources
- Power BI Performance Analyzer
- DAX Studio for model optimization
- SQL Server Profiler for source query analysis
- Power BI Community forums

## Next Steps
1. Run Query Diagnostics on problematic models
2. Identify top 3 slowest queries
3. Implement quick wins first
4. Schedule workshop with domain teams
5. Create optimization template/checklist
