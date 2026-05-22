import bpy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Taro Kamata",
    "version": (4, 4),
    "blender": (4, 4, 0),
    "location": "",
    "description": "レベルエディタ",
    "category": "Object",
    "support": 'Testing',
    "doc_url": "{BLENDER_MANUAL_URL}/addons/animation/copy_global_transform.html",
}

# アドオン有効化時コールバック
def register():
    print ("レベルエディタが有効化されました")

# アドオン無効化時コールバック
def unregister():
    print ("レベルエディタが無効化されました")

# テスト用実行コード
if __name__== "__main__":
    register()
