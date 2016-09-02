CREATE TABLE wifsippressure(
 datemeas timestamp,
 counts integer,
 volts real,
 mbar real,
 temp0 real,
 temp1 real,
 temp2 real,
 temp3 real,
 PRIMARY KEY (datemeas)
);

COMMENT ON TABLE wifsippressure IS 'JSON data collection from the WiFSIP pressure sensor';
COMMENT ON COLUMN wifsippressure.datemeas IS 'timestamp of pressure measurement';
COMMENT ON COLUMN wifsippressure.counts IS '[ADU] counts of pressure measurement';
COMMENT ON COLUMN wifsippressure.volts IS '[V] volts converted from ADUs';
COMMENT ON COLUMN wifsippressure.mbar IS '[mBar] pressure converted from volts';
COMMENT ON COLUMN wifsippressure.temp0 IS '[deg C] dewar temperature';
COMMENT ON COLUMN wifsippressure.temp1 IS '[deg C] coldhead temperature';
