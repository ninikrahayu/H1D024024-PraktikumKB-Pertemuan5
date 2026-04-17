import tkinter as tk
from tkinter import ttk, messagebox

gejala = {
    "G1": "Nafas abnormal", 
    "G2": "Suara serak", 
    "G3": "Perubahan kulit", 
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan", 
    "G6": "Nyeri tenggorokan", 
    "G7": "Nyeri leher", 
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging", 
    "G10": "Air liur menetes", 
    "G11": "Perubahan suara", 
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung", 
    "G14": "Vertigo", 
    "G15": "Getah bening", 
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat", 
    "G18": "Infeksi sinus", 
    "G19": "Berat badan turun", 
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah", 
    "G22": "Benjolan leher", 
    "G23": "Tubuh tak seimbang", 
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah", 
    "G26": "Dahi sakit", 
    "G27": "Batuk", 
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher", 
    "G30": "Nyeri antara mata", 
    "G31": "Radang telinga", 
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler", 
    "G34": "Tuli", 
    "G35": "Mual muntah", 
    "G36": "Letih lesu", 
    "G37": "Demam"
}

penyakit = {
    "Tonsilitis": ["G37","G12","G5","G27","G6","G21"],
    "Sinusitis Maksilaris": ["G37","G12","G27","G17","G33","G36","G29"],
    "Sinusitis Frontalis": ["G37","G12","G27","G17","G33","G36","G21","G26"],
    "Sinusitis Etmoidalis": ["G37","G12","G27","G17","G33","G36","G21","G30","G13","G26"],
    "Sinusitis Sfenoidalis": ["G37","G12","G27","G17","G33","G36","G29","G7"],
    "Abses Peritonsiler": ["G37","G12","G6","G15","G2","G29","G10"],
    "Faringitis": ["G37","G5","G6","G7","G15"],
    "Kanker Laring": ["G5","G27","G6","G15","G2","G19","G1"],
    "Deviasi Septum": ["G37","G17","G20","G8","G18","G25"],
    "Laringitis": ["G37","G5","G15","G16","G32"],
    "Kanker Leher & Kepala": ["G5","G22","G8","G28","G3","G11"],
    "Otitis Media Akut": ["G37","G20","G35","G31"],
    "Contact Ulcers": ["G5","G2"],
    "Abses Parafaringeal": ["G5","G16"],
    "Barotitis Media": ["G12","G20"],
    "Kanker Nasofaring": ["G17","G8"],
    "Kanker Tonsil": ["G6","G29"],
    "Neuronitis Vestibularis": ["G35","G24"],
    "Meniere": ["G20","G35","G14","G4"],
    "Tumor Syaraf Pendengaran": ["G12","G34","G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34","G9"],
    "Vertigo Postular": ["G24"]
}

class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("500x650")

        self.vars = {}
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Diagnosa Penyakit THT",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Pilih gejala yang Anda rasakan:",
                 font=("Arial", 10)).pack()

        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True, padx=20)

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for kode, nama in gejala.items():
            var = tk.BooleanVar()
            self.vars[kode] = var

            tk.Checkbutton(scroll_frame,
                           text=f"{kode} - {nama}",
                           variable=var).pack(anchor="w")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Button(self.root, text="PROSES DIAGNOSA",
                  command=self.proses_diagnosa,
                  bg="green", fg="white").pack(fill="x", padx=20, pady=10)

        tk.Button(self.root, text="RESET",
                  command=self.reset,
                  bg="red", fg="white").pack(fill="x", padx=20)

    def reset(self):
        for var in self.vars.values():
            var.set(False)

    def proses_diagnosa(self):
        input_gejala = [k for k, v in self.vars.items() if v.get()]

        if not input_gejala:
            messagebox.showwarning(
                "Input Tidak Valid",
                "Silakan pilih minimal satu gejala!"
            )
            return

        hasil = {}

        for p, g_list in penyakit.items():
            cocok = sum(1 for g in g_list if g in input_gejala)
            persen = (cocok / len(g_list)) * 100
            hasil[p] = persen

        ranking = sorted(hasil.items(), key=lambda x: x[1], reverse=True)

        terbaik, nilai = ranking[0]

        if nilai == 0:
            messagebox.showinfo("Hasil", "Tidak ada penyakit yang cocok.")
        else:
            text = f"Hasil Utama:\n{terbaik} ({round(nilai,2)}%)\n\nRanking:\n"
            for p, v in ranking:
                if v > 0:
                    text += f"- {p} ({round(v,2)}%)\n"

            messagebox.showinfo("Hasil Diagnosa", text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()