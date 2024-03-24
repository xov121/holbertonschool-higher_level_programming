-- Ensure we're operating on the correct database
USE hbtn_0d_usa;

-- Create the cities table with a relationship to states
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id)
);
