import random
import tkinter as tk
from tkinter import ttk, messagebox
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("700x600")  
        self.root.resizable(False, False)
        
        self.root.configure(bg='#2c3e50')
        
        self.setup_styles()

        self.create_widgets()
        
        try:
            self.generate_password()
        except:
            pass 
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Title.TLabel', 
                       font=('Arial', 20, 'bold'), 
                       background='#2c3e50', 
                       foreground='#ecf0f1')
        
        style.configure('Subtitle.TLabel', 
                       font=('Arial', 12), 
                       background='#2c3e50', 
                       foreground='#bdc3c7')
        
        style.configure('Custom.TFrame', 
                       background='#2c3e50')
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style='Custom.TFrame', padding="30")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="Password Generator", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 10))
        
        subtitle_label = ttk.Label(main_frame, text="Generate secure passwords", 
                                  style='Subtitle.TLabel')
        subtitle_label.pack(pady=(0, 30))
        
        # Password length section
        length_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        length_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(length_frame, text="Password Length:", 
                 font=('Arial', 11, 'bold'), 
                 background='#2c3e50', 
                 foreground='#ecf0f1').pack(side=tk.LEFT)
        
        self.length_var = tk.IntVar(value=12)
        length_scale = tk.Scale(length_frame, from_=4, to=64, 
                               orient=tk.HORIZONTAL, 
                               variable=self.length_var,
                               bg='#34495e', fg='#ecf0f1',
                               highlightbackground='#2c3e50',
                               troughcolor='#95a5a6',
                               activebackground='#3498db',
                               length=200)
        length_scale.pack(side=tk.RIGHT)
        
        self.length_display = ttk.Label(length_frame, text="12", 
                                       font=('Arial', 11, 'bold'),
                                       background='#2c3e50', 
                                       foreground='#e74c3c')
        self.length_display.pack(side=tk.RIGHT, padx=(0, 10))
        
        length_scale.configure(command=self.update_length_display)
        
        options_frame = ttk.LabelFrame(main_frame, text="Character Options", 
                                      padding="15")
        options_frame.pack(fill=tk.X, pady=(0, 20))

        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.exclude_ambiguous = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(options_frame, text="Lowercase (a-z)", 
                       variable=self.include_lowercase,
                       command=self.on_option_change).grid(row=0, column=0, sticky=tk.W, pady=2)
        
        ttk.Checkbutton(options_frame, text="Uppercase (A-Z)", 
                       variable=self.include_uppercase,
                       command=self.on_option_change).grid(row=1, column=0, sticky=tk.W, pady=2)
        
        ttk.Checkbutton(options_frame, text="Numbers (0-9)", 
                       variable=self.include_numbers,
                       command=self.on_option_change).grid(row=0, column=1, sticky=tk.W, pady=2)
        
        ttk.Checkbutton(options_frame, text="Symbols (!@#$%...)", 
                       variable=self.include_symbols,
                       command=self.on_option_change).grid(row=1, column=1, sticky=tk.W, pady=2)
        
        ttk.Checkbutton(options_frame, text="Exclude similar chars", 
                       variable=self.exclude_ambiguous,
                       command=self.on_option_change).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=2)
        
        display_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        display_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(display_frame, text="Generated Password:", 
                 font=('Arial', 11, 'bold'),
                 background='#2c3e50', 
                 foreground='#ecf0f1').pack(anchor=tk.W)
        
        self.password_var = tk.StringVar()
        password_frame = tk.Frame(display_frame, bg='#2c3e50')
        password_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.password_entry = tk.Entry(password_frame, 
                                      textvariable=self.password_var,
                                      font=('Courier New', 14, 'bold'),
                                      bg='#ecf0f1', 
                                      fg='#2c3e50',
                                      relief=tk.FLAT,
                                      bd=0,
                                      state='readonly',
                                      readonlybackground='#ecf0f1')
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
 
        copy_btn = tk.Button(password_frame, text="Copy", 
                           command=self.copy_password,
                           bg='#3498db', fg='white',
                           font=('Arial', 10, 'bold'),
                           relief=tk.FLAT,
                           padx=15, pady=5,
                           cursor='hand2')
        copy_btn.pack(side=tk.RIGHT)
  
        self.strength_var = tk.StringVar(value="Strength: Not Generated")
        self.strength_label = tk.Label(display_frame, textvariable=self.strength_var,
                                      font=('Arial', 12, 'bold'),
                                      bg='#2c3e50',
                                      fg='#ffffff')
        self.strength_label.pack(pady=(5, 0))
        
        buttons_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        buttons_frame.pack(fill=tk.X, pady=(0, 20))
        
        generate_btn = tk.Button(buttons_frame, text="Generate Password", 
                               command=self.generate_password,
                               bg='#27ae60', fg='white',
                               font=('Arial', 12, 'bold'),
                               relief=tk.FLAT,
                               padx=20, pady=10,
                               cursor='hand2')
        generate_btn.pack(side=tk.LEFT, padx=(0, 10))

        clear_btn = tk.Button(buttons_frame, text="Clear", 
                            command=self.clear_password,
                            bg='#e74c3c', fg='white',
                            font=('Arial', 12, 'bold'),
                            relief=tk.FLAT,
                            padx=20, pady=10,
                            cursor='hand2')
        clear_btn.pack(side=tk.LEFT)
    
    def update_length_display(self, value):
        self.length_display.configure(text=str(value))
        self.on_option_change()
    
    def on_option_change(self):
        if hasattr(self, 'password_var') and hasattr(self, 'strength_var'):
            self.generate_password()
    
    def get_character_set(self):
        characters = ""
        
        if self.include_lowercase.get():
            chars = string.ascii_lowercase
            if self.exclude_ambiguous.get():
                chars = chars.replace('l', '').replace('o', '')
            characters += chars
            
        if self.include_uppercase.get():
            chars = string.ascii_uppercase
            if self.exclude_ambiguous.get():
                chars = chars.replace('I', '').replace('O', '')
            characters += chars
            
        if self.include_numbers.get():
            chars = string.digits
            if self.exclude_ambiguous.get():
                chars = chars.replace('0', '').replace('1', '')
            characters += chars
            
        if self.include_symbols.get():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        return characters
    
    def generate_password(self):
        try:
            length = self.length_var.get()
            characters = self.get_character_set()
            
            if not characters:
                messagebox.showerror("Error", "Select at least one character type!")
                return
                
            if length < 1:
                messagebox.showerror("Error", "Length must be at least 1!")
                return
            
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)

            if hasattr(self, 'strength_var') and hasattr(self, 'strength_label'):
                self.update_password_strength(password)
            
        except Exception as e:
            print(f"Error generating password: {e}")  # Debug print
            messagebox.showerror("Error", f"Could not generate password: {str(e)}")
    
    def update_password_strength(self, password):
        if not hasattr(self, 'strength_var') or not hasattr(self, 'strength_label'):
            return
            
        score = 0
        
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
        
        if score >= 6:
            strength = "Very Strong"
            color = "#00ff00"  
        elif score >= 4:
            strength = "Strong"
            color = "#ffff00" 
        elif score >= 2:
            strength = "Medium"
            color = "#ff8800"
        else:
            strength = "Weak"
            color = "#ff0000"
        
        self.strength_var.set(f"Strength: {strength}")
        self.strength_label.configure(fg=color)
    
    def copy_password(self):
        password = self.password_var.get()
        if password:
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append(password)
                self.root.update()
                messagebox.showinfo("Success", "Password copied!") 
            except Exception as e:
                messagebox.showerror("Error", f"Copy failed: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def clear_password(self):
        self.password_var.set("")
        self.strength_var.set("Strength: Not Generated")
        self.strength_label.configure(fg='#ffffff')

def main():
    print("Starting Password Generator...")
    root = tk.Tk()
    print("Window created")
    app = PasswordGenerator(root)
    print("App initialized, starting main loop...")
    root.mainloop()
    print("App closed")

if __name__ == "__main__":
    main()
