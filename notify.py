import pyinotify

wm = pyinotify.WatchManager()  # 创建WatchManager对象
wm.add_watch('/tmp', pyinotify.ALL_EVENTS)  # 添加要监控的目录，以及要监控的事件，这里ALL_EVENT表示所有事件

notifier = pyinotify.Notifier(wm)  # 交给Notifier进行处理
notifier.loop()  # 循环处理事件