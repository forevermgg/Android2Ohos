# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 获得当前目录
print(os.getcwd())
# 获取src下所有文件
__src__files = os.listdir(os.getcwd() + "/layout/src/")
# 打印文件集合
print(__src__files)
# 获取替换规则
# https://www.box3.cn/tools/addslashes.html 在线字符串转义
MAP_END = "forevermgg:end"
Map = {
    # head
    "xmlns:android": "xmlns:ohos",
    "http://schemas.android.com/apk/res/android": "http://schemas.huawei.com/res/ohos",
    "xmlns:tools=\"http://schemas.android.com/tools\"": "\n\r",
    "android:id": "ohos:id",
    "@+id/": "$+id:",
    "@color/": "$color:",
    "@drawable/": "$graphic:",
    "@string/": "$string:",

    # width height
    "android:layout_width": "ohos:width",
    "android:layout_height": "ohos:height",
    "wrap_content": "match_content",

    # alignParent
    "android:layout_alignParentLeft": "ohos:align_parent_left",
    "android:layout_alignParentRight": "ohos:align_parent_right",
    "android:layout_alignParentTop": "ohos:align_parent_top",
    "android:layout_alignParentBottom": "ohos:align_parent_bottom",
    "android:layout_alignParentStart": "ohos:align_parent_start",
    "android:layout_alignParentEnd": "ohos:align_parent_end",

    # padding
    "android:paddingStart": "ohos:start_padding",
    "android:paddingEnd": "ohos:end_padding",
    "android:paddingLeft": "ohos:left_padding",
    "android:paddingRight": "ohos:right_padding",
    "android:paddingTop": "ohos:top_padding",
    "android:paddingBottom": "ohos:bottom_padding ",
    "android:padding": "ohos:padding",

    # margin
    "android:layout_marginLeft": "ohos:left_margin",
    "android:layout_marginRight": "ohos:right_margin",
    "android:layout_marginTop": "ohos:top_margin",
    "android:layout_marginBottom": "ohos:bottom_margin ",

    # background
    "android:background": "ohos:background_element",

    # text
    "<TextView": "<Text",
    "</TextView>": "</Text>",
    "android:textColor": "ohos:text_color",
    "android:textSize": "ohos:text_size",
    "android:singleLine": "ohos:max_text_lines",
    "android:text": "ohos:text",
    "android:drawableLeft": "ohos:element_left",
    "android:drawableRight": "ohos:element_right",
    "android:drawablePadding": "ohos:element_padding",
    "android:maxLines=\"1\"": "ohos:max_text_lines=\"1\"",

    # image
    "<ImageView": "<Image",
    "</ImageView>": "<Image>",
    "android:src": "ohos:image_src",

    # DependentLayout
    "<RelativeLayout": "<DependentLayout",
    "</RelativeLayout>": "</DependentLayout>",
    "android:layout_below": "ohos:below",
    "android:layout_toRightOf": "ohos:right_of",

    # DirectionalLayout
    "<LinearLayout": "<DirectionalLayout",
    "</LinearLayout>": "</DirectionalLayout>",
    "android:layout_weight": "ohos:weight",

    # TextField
    "<EditText": "<TextField",
    "</EditText>": "</TextField>",

    # listContainer
    "<android.support.v7.widget.RecyclerView": "<ListContainer",
    "</android.support.v7.widget.RecyclerView>": "</ListContainer>",

    # orientation
    "android:orientation": "ohos:orientation",
    "android:layout_gravity": "ohos:layout_alignment",

    # gravity->alignment
    "android:gravity": "ohos:alignment",

    # visibility
    "android:visibility": "ohos:visibility",
    "gone": "hide",

    "android:layout_centerVertical": "ohos:vertical_center",
    "center_vertical": "vertical_center",
    "center_horizontal": "horizontal_center",

    "android:focusable=\"true\"": "ohos:focusable=\"focus_enable\"",
    "android:focusableInTouchMode=\"true\"": "ohos:focusable_in_touch=\"true\"",

    # ProgressBar
    "android:max=\"100\"": "ohos:max=\"100\"",
    "android:progress=\"100\"": "ohos:progress=\"100\"",
    # map替换结束符，在此执行写文件操作
    MAP_END: "end"
}
# 遍历所有文件进行替换操作
for file in __src__files:
    # 当前替换操作文件
    print(str(file))
    file_read = open(os.getcwd() + "/layout/src/" + str(file), "r", encoding="utf-8")
    # 将文件内容保存到内存
    lines = file_read.readlines()
    file_write = open(os.getcwd() + "/layout/des/" + str(file), "w", encoding="utf-8")
    for line in lines:
        for key, value in Map.items():
            if key in line:
                line = line.replace(key, value)  # 新内容代替旧内容
                if key == MAP_END:
                    file_write.write(line)
            else:
                if key == MAP_END:
                    file_write.write(line)
    file_write.close()
    file_read.close()
