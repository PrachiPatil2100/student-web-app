from flask import Flask, render_template, request, redirect, url_for,flash
import sqlite3

app = Flask(__name__)
app.secret_key = "prachi_super_secret_key"

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    error_msg = None
    if request.method == 'POST':
        form_name = request.form['name']
        form_age = int(request.form['age'])
        form_roll = int(request.form['roll_number'])
        if form_age <= 0 or form_roll <= 0:
            error_msg = "⚠️ Error: Age and Roll Number must be positive numbers!"
        else:
            conn = get_db_connection()
        try:
            conn.execute('INSERT INTO students (name, age, roll_number) VALUES (?, ?, ?)',
                         (form_name, form_age, form_roll))
            conn.commit()
            flash(f"✅ Success: {form_name} (Roll: {form_roll}) has been added!", "success")
        except sqlite3.IntegrityError:
            error_msg = "⚠️ Error: Yeh Roll Number pehle se kisi aur student ka hai!"
        finally:
            conn.close()
            
    search_query = request.args.get('search') 
    
    conn = get_db_connection()
    if search_query:
        students_from_db = conn.execute('SELECT * FROM students WHERE roll_number = ?', (search_query,)).fetchall()
        if not students_from_db:
            error_msg = f"❌ No student found with Roll Number: {search_query}"
    else:
        students_from_db = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
        
    return render_template('index.html', students=students_from_db, error=error_msg)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    student = conn.execute('SELECT name FROM students WHERE id = ?', (id,)).fetchone()
    if student:
        student_name = student['name']

        conn.execute('DELETE FROM students WHERE id = ?', (id,))
        conn.commit()

        flash(f"🗑️ Success: {student_name}'s record has been permanently deleted.", "success")

        conn.close()
        return redirect(url_for('home'))
    
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    error_msg = None
    
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = int(request.form['age'])
        
        conn.execute('UPDATE students SET name = ?, age = ? WHERE id = ?',
                     (new_name, new_age, id))
        conn.commit()
        conn.close()
       
        flash("✅ Student details updated successfully!", "success")
        return redirect(url_for('home'))
        
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    return render_template('edit.html', student=student, error=error_msg)
   
if __name__ == '__main__':
    app.run(debug=True)