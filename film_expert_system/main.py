from tkinter import *
from pyswip import Prolog

class FilmExpertSystem:
    def __init__(self, master):
        self.master = master
        master.title("Sistem Pakar Rekomendasi Film Berdasarkan Mood")

        self.label = Label(master, text="Pilih Mood Kamu:")
        self.label.pack(pady=10)

        self.mood_var = StringVar()
        self.mood_options = ["senang", "sedih", "bosan", "romantis", "semangat"]

        for mood in self.mood_options:
            Radiobutton(master, text=mood.capitalize(), variable=self.mood_var, value=mood).pack(anchor=W)

        self.submit_button = Button(master, text="Lihat Rekomendasi", command=self.get_recommendation)
        self.submit_button.pack(pady=10)

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack(pady=10)

        self.prolog = Prolog()
        self.prolog.consult("knowledge.pl")

    def get_recommendation(self):
        mood = self.mood_var.get()
        self.result_text.delete(1.0, END)

        if not mood:
            self.result_text.insert(END, "⚠️ Silakan pilih mood terlebih dahulu.\n")
            return

        query = f"rekomendasi({mood}, Film)"
        results = list(self.prolog.query(query))

        if results:
            self.result_text.insert(END, f"🎥 Rekomendasi untuk mood '{mood}':\n\n")
            for res in results:
                self.result_text.insert(END, f"- {res['Film']}\n")
        else:
            self.result_text.insert(END, "😕 Tidak ditemukan rekomendasi untuk mood tersebut.")

if __name__ == "__main__":
    root = Tk()
    app = FilmExpertSystem(root)
    root.mainloop()