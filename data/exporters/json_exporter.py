import json

# لیست از دیکشنری‌ها
# data = [
#     {"address": "123 Main St", "name": "John Doe", "age": 30},
#     {"address": "456 Oak St", "name": "Jane Smith", "age": 25},
#     {"address": "789 Pine St", "name": "Alice Johnson", "age": 35}
# ]

# # ذخیره داده‌ها در یک فایل JSON
# with open('output.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)

# print("Data has been written to output.json")




def json_exporter(OUTPUT_LIST, FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as json_file:
        if isinstance(OUTPUT_LIST, dict):
            json.dump(OUTPUT_LIST, json_file, ensure_ascii=False, indent=4)
        
        elif isinstance(OUTPUT_LIST, list):
            # تبدیل لیست به دیکشنری با ایندکس
            data = {str(i): OUTPUT_LIST[i] for i in range(len(OUTPUT_LIST))}
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        else:
            raise TypeError("OUTPUT_LIST must be dict or list")