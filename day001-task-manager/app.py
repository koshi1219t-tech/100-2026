import json

tasks = []

with open("tasks.json","r", encoding="utf-8") as file:
    tasks = json.load(file)

while True:
    print("\n=== タスク管理 ===")
    print("1. 一覧を見る")
    print("2. タスクを追加する")
    print("3. タスクを削除する")
    print("4. タスクの完了・未完了を切り替える")
    print("5. 終了する")

    choice = input("選択してください:")

    if choice =="1":
        
        if len(tasks) == 0:
            print("表示出来るタスクはありません。")
            continue

        for i, task in enumerate(tasks):
            status = "完了" if task["completed"] else "未完了"
            print(f"{i+1}. [{status}] {task['title']}")

    elif choice =="2":
        title = input("追加するタスクを入力してください:")

        if title == "":
            print("空のタスクは追加できません。")
            continue

        new_task = {
            "title": title,
            "completed": False
        }

        tasks.append(new_task)

        with open("tasks.json","w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

        print("タスクを追加しました:", title)

    elif choice == "3":

        if len(tasks) == 0:
            print("削除できるタスクがありません。")
            continue

        for i, task in enumerate(tasks):
            status = "完了" if task["completed"] else "未完了"
            print(f"{i+1}. [{status}] {task['title']}")

        try:
            delete_number = int(input("削除するタスク番号を入力してください:"))
        except ValueError:
            print("無効な入力です。数字を入力してください。")
            continue

        delete_index = delete_number - 1

        if delete_index < 0 or delete_index >= len(tasks):
            print("無効な番号です。")
            continue

        deleted_task = tasks.pop(delete_index)

        with open("tasks.json","w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
        print("タスクを削除しました:", deleted_task["title"])

    elif choice == "4":
        if len(tasks) == 0:
            print("完了・未完了を切り替えることができるタスクがありません。")
            continue

        for i, task in enumerate(tasks):
            status = "完了" if task["completed"] else "未完了"
            print(f"{i+1}. [{status}] {task['title']}")

        try:
            number = int(input("完了・未完了を切り替えるタスク番号を入力してください:"))
        except ValueError:
            print("無効な入力です。数字を入力してください。")
            continue
        index = number - 1

        tasks[index]["completed"] = not tasks[index]["completed"]

        with open("tasks.json","w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

        print("変更しました。", tasks[index]["title"])

    elif choice == "5":
        print("終了します。")
        break   

    else:
        print("無効な選択です。１〜５の数字を入力してください。")
