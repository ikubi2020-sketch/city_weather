import React, { useState, useEffect } from 'react';

export default function () {
    const [userName, setUserName] = useState(() => {
    const saved = localStorage.getItem('userName');
    return saved ? JSON.parse(saved) : '';
    });    

  return (
    <div>
        <h1>ברוכים הבאים לאתר מזג האויור</h1>
        <h2>על מנת לגשת לאתר הכנס שם משתמש</h2>
        <input type="text" placeholder="השם שלך" 
        value={userName}
        onChange={e => setUserName(e.target.value)}/>
    </div>
  )
}
