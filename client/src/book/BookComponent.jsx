import React, { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/knjige/";

const BookTable = () => {
  const [books, setBooks] = useState([]);
  const [newBook, setNewBook] = useState({
    naslov: "",
    isbn: "",
    godina_izdanja: "",
    dostupna: true,
    autor_id: 1,
  });

  useEffect(() => {
    fetchBooks();
  }, []);

  


  const fetchBooks = async () => {
    try {
     

      const res = await fetch(API_URL);
      if (!res.ok) throw new Error("Greška pri učitavanju knjiga!");
      const data = await res.json();
      setBooks(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error(err);
      setBooks([]);
    }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setNewBook({
      ...newBook,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validacija
    if (!newBook.naslov.trim() || !newBook.isbn.trim() || !newBook.godina_izdanja || !newBook.autor_id) {
      alert("Sva polja su obavezna!");
      return;
    }

    const godina = parseInt(newBook.godina_izdanja, 10);
    const autorId = parseInt(newBook.autor_id, 10);

    if (isNaN(godina) || godina < 1000 || godina > 2100) {
      alert("Unesi validnu godinu izdanja (1000-2100).");
      return;
    }

    if (isNaN(autorId)) {
      alert("Unesi validan ID autora.");
      return;
    }

    const payload = {
      naslov: newBook.naslov.trim(),
      isbn: newBook.isbn.trim(),
      godina_izdanja: godina,
      dostupna: Boolean(newBook.dostupna),
      autor_id: autorId,
    };

    console.log("Šaljem payload:", payload); // <- ovo će ti pokazati šta ide na backend

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const errData = await res.json();
        console.error("Greška sa servera:", errData);
        throw new Error("Greška pri dodavanju knjige!");
      }

      const addedBook = await res.json();
      setBooks([...books, addedBook]);
      setNewBook({ naslov: "", isbn: "", godina_izdanja: "", dostupna: true, autor_id: 1 });
    } catch (err) {
      console.error(err);
      alert("❌ Nije moguće dodati knjigu!");
    }
  };

  return (
    <div className="table-container">
      <h2>📚 Lista knjiga</h2>

      <table className="book-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Naslov</th>
            <th>ISBN</th>
            <th>Godina</th>
            <th>Dostupna</th>
            <th>Autor ID</th>
          </tr>
        </thead>
        <tbody>
          {books.length ? books.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.naslov}</td>
              <td>{book.isbn}</td>
              <td>{book.godina_izdanja}</td>
              <td>{book.dostupna ? "Da" : "Ne"}</td>
              <td>{book.autor?.id || book.autor_id}</td>
            </tr>
          )) : (
            <tr><td colSpan="6">Nema dostupnih knjiga.</td></tr>
          )}
        </tbody>
      </table>

      <form onSubmit={handleSubmit} className="book-form">
        <h3>➕ Dodaj novu knjigu</h3>
        <label>
          Naslov:
          <input type="text" name="naslov" value={newBook.naslov} onChange={handleChange} required />
        </label>
        <label>
          ISBN:
          <input type="text" name="isbn" value={newBook.isbn} onChange={handleChange} required />
        </label>
        <label>
          Godina izdanja:
          <input type="number" name="godina_izdanja" value={newBook.godina_izdanja} onChange={handleChange} required />
        </label>
        <label>
          Dostupna:
          <input type="checkbox" name="dostupna" checked={newBook.dostupna} onChange={handleChange} />
        </label>
        <label>
          Autor ID:
          <input type="number" name="autor_id" value={newBook.autor_id} onChange={handleChange} required />
        </label>
        <button type="submit">➕ Dodaj knjigu</button>
      </form>
    </div>
  );
};

export default BookTable;
