-- Every citation points at an existing concept and an existing source.
WITH c AS (
  SELECT id FROM principles UNION ALL SELECT id FROM architectures UNION ALL SELECT id FROM practices
)
SELECT 'concept_id' AS end_, concept_id AS missing_id FROM concept_sources WHERE concept_id NOT IN (SELECT id FROM c)
UNION ALL
SELECT 'source_id', source_id FROM concept_sources WHERE source_id NOT IN (SELECT id FROM sources);
