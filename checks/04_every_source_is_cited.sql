-- A source nobody cites is dead weight.
SELECT id FROM sources WHERE id NOT IN (SELECT source_id FROM concept_sources);
