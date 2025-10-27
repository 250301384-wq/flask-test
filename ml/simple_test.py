print("=== 开始数据处理测试 ===")

try:
    import pandas as pd
    print(" pandas 导入成功")
    
    # 测试 v1 数据集
    df1 = pd.read_csv("data/raw/news_v1.csv")
    print(f" v1 数据集加载成功: {len(df1)} 条记录")
    print(f"  - 类别: {df1['category'].tolist()}")
    
    # 测试 v2 数据集
    df2 = pd.read_csv("data/raw/news_v2.csv") 
    print(f" v2 数据集加载成功: {len(df2)} 条记录")
    print(f"  - 类别: {df2['category'].tolist()}")
    
    print(" 所有测试通过！")
    
except Exception as e:
    print(f" 测试失败: {e}")
    import traceback
    traceback.print_exc()
