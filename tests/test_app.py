from flask import Flask, jsonify, request
from config import get_settings


# 加载配置
settings = get_settings()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "欢迎使用新闻分类系统！",
        "status": "运行正常",
        "version": "1.0.0"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/classify', methods=['POST'])
def classify_news():
    """新闻分类接口"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "请提供新闻文本"}), 400
        print(data)

        text = data['text']
        print(text)
        
        # 这里是模拟分类结果，后续会替换为真实模型
        categories = ["体育", "科技", "政治", "娱乐", "财经"]
        simulated_category = categories[len(text) % len(categories)]
        confidence = 0.85
        
        return jsonify({
            "category": simulated_category,
            "confidence": confidence,
            "text_length": len(text)
        })
        
    except Exception as e:
        return jsonify({"error": f"处理请求时出错: {str(e)}"}), 500



if __name__ == '__main__':
    app.run(
        host=settings.host,
        port=settings.port,
        debug=settings.debug
    )
