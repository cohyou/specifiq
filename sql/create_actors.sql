CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP DEFAULT (DATETIME('now','localtime')),
    modified_at TIMESTAMP DEFAULT (DATETIME('now','localtime')),
    creator VARCHAR(256) NOT NULL DEFAULT '',
    modifier VARCHAR(256) NOT NULL DEFAULT ''
);
