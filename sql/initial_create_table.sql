USE telegram;
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    sender_id BIGINT NOT NULL,
    message_text TEXT NOT NULL
);
