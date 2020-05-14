CREATE TRIGGER userstate_changed
AFTER INSERT OR UPDATE
ON quant_userstate
FOR EACH ROW
EXECUTE PROCEDURE notify_userstate_changes()