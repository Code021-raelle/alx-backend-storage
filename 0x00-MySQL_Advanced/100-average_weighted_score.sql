-- Create a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;

    SELECT SUM(p.weight) INTO total_weight
    FROM projects p
    JOIN corrections c ON p.id = c.project_id
    WHERE c.user_id = user_id;

    SELECT SUM(p.weight * c.score) INTO weighted_score_sum
    FROM projects p
    JOIN corrections c ON p.id = c.project_id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        SET avg_weighted_score = weighted_score_sum / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END if;

    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //

DELIMITER ;
