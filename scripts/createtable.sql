CREATE TABLE wifsippressure(
 datemeas timestamp,
 counts integer,
 volts real,
 mbar real,
 PRIMARY KEY (datemeas)
);

COMMENT ON TABLE wifsippressure IS 'JSON data collection from the WiFSIP pressure sensor';
COMMENT ON COLUMN wifsippressure.datemeas IS 'timestamp of pressure measurement';
COMMENT ON COLUMN wifsippressure.counts IS '[ADU] counts of pressure measurement';
COMMENT ON COLUMN wifsippressure.volts IS '[V] volts converted from ADUs';
COMMENT ON COLUMN wifsippressure.volts IS '[mBar] pressure converted from volts';
