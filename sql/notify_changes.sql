CREATE OR REPLACE FUNCTION notify_userstate_changes()
RETURNS trigger AS $$
BEGIN
    PERFORM pg_notify(
        'userstate_changed',
        json_build_object(
            'operation', TG_OP,
            'record', row_to_json(NEW)
        )::text
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER userstate_changed
AFTER INSERT OR UPDATE
ON quant_userstate
FOR EACH ROW
EXECUTE PROCEDURE notify_userstate_changes()