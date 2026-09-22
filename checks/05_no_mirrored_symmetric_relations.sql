-- pairs-with and same-family-as are symmetric: store each pair once.
SELECT a.from_id, a.to_id, a.relation
FROM relations a
JOIN relations b ON a.from_id = b.to_id AND a.to_id = b.from_id AND a.relation = b.relation
WHERE a.relation IN ('pairs-with', 'same-family-as') AND a.from_id < a.to_id;
