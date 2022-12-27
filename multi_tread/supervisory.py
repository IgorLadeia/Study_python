# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from multi_tread import rotina_shell


"""classe recomendada pelo desenvolvedor da biblioteca, para o monitoramento do diretório escolhido"""
class OnMyWatch:
    # Set the directory on watch
    watchDirectory = r"\\global.scd.scania.com\proj\P\Pamfiles\Prod\scim"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


"""
classe recomendada pelo desenvolvedor da biblioteca, onde é especificado os modo de monitoramento escolhidos 
alguns modos de monitoramento geram mutiplicidade de comando. Sendo assim, é utilizado apenas 3 desses modos 
para haver o menor numero de mutiplicidade de comandos (arquivo criado, arquivo atualizado, arquivo deletado)
"""
class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            rotina_shell.atualization_dic.created_event((event.src_path))


        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            rotina_shell.atualization_dic.modified_event(event.src_path)


        elif event.event_type == 'deleted':
            print("Watchdog received deleted event - % s." % event.src_path)
            rotina_shell.atualization_dic.deleted_event((event.src_path))


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
