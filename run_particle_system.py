import http.server
import socketserver
import webbrowser
import os
import sys

# 设置端口
PORT = 8000

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 目标 HTML 文件
html_file = "particle_gesture_system.html"

# 切换工作目录到脚本所在目录
os.chdir(current_dir)

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/{html_file}"
        print(f"正在启动服务器: {url}")
        print("请在浏览器中允许摄像头权限以使用手势控制。")
        print("按 Ctrl+C 停止服务器。")
        
        # 自动打开浏览器
        webbrowser.open(url)
        
        httpd.serve_forever()
except OSError as e:
    if e.errno == 10048:
        print(f"端口 {PORT} 被占用，请尝试更改端口或关闭占用端口的程序。")
    else:
        print(f"发生错误: {e}")
except KeyboardInterrupt:
    print("\n服务器已停止。")
