CREATE TABLE requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT NOT NULL DEFAULT '',
    parent INTEGER,
    created_at TIMESTAMP DEFAULT (DATETIME('now','localtime')),
    modified_at TIMESTAMP DEFAULT (DATETIME('now','localtime')),
    creator VARCHAR(256) NOT NULL DEFAULT '',
    modifier VARCHAR(256) NOT NULL DEFAULT ''
);
