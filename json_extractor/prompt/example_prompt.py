DOCLING_EXAMPLE = """
Raw Data:
## A1. 個案婚姻狀況：
□ 1. 離婚
 2. 分居
□ 3. 喪偶
## A2. 年齡：
50

Template:
{
  "A1": {
    "個案婚姻狀況": [
      { "離婚": 0 },
      { "分居": 0 },
      { "喪偶": 0 }
    ]
  },
  "A2": {
    "年齡": ""
  }
}

Expected Output:
{
  "A1": {
    "個案婚姻狀況": [
      { "離婚": 0 },
      { "分居": 1 },
      { "喪偶": 0 }
    ]
  },
  "A2": {
    "年齡": "50"
  }
}
"""