import os
from PIL import Image

def convert_to_webp_recursive():
    # 获取脚本所在的根目录 (比如你的 source/img)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    count = 0
    
    # 使用 os.walk 开启“全自动巡航”，它会遍历里面所有的小文件夹！
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            # 锁定目标格式
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, filename)
                # 拼凑出新的 webp 文件名
                webp_name = filename.rsplit('.', 1)[0] + '.webp'
                webp_path = os.path.join(root, webp_name)
                
                # 如果还没被转换过，就干活
                if not os.path.exists(webp_path):
                    try:
                        with Image.open(file_path) as img:
                            img.save(webp_path, 'webp', quality=80)
                            # 打印出相对路径，让你看清楚是哪个子文件夹里的图被转换了
                            rel_path = os.path.relpath(webp_path, base_dir)
                            print(f"✨ 巡航压缩成功: {rel_path}")
                            count += 1
                    except Exception as e:
                        print(f"❌ 转换 {filename} 失败: {e}")
                        
    print(f"\n🎉 搞定！本次管线共在所有文件夹中为你转换了 {count} 张 WebP 图片。")

if __name__ == "__main__":
    print("🚀 启动全自动递归压缩管线 (V2.0)...")
    convert_to_webp_recursive()
    input("按回车键退出...")