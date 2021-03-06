--------------------------------------------------------
--  颇老捞 积己凳 - 老夸老-7岿-08-2018   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table PC
--------------------------------------------------------

  CREATE TABLE "DBSTUDY"."PC" 
   (	"MODEL" NUMBER(*,0), 
	"SPEED" NUMBER(*,0), 
	"RAM" NUMBER(*,0), 
	"HD" NUMBER, 
	"CD" CHAR(20 BYTE), 
	"PRICE" NUMBER(*,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
REM INSERTING into DBSTUDY.PC
SET DEFINE OFF;
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1001,133,16,1.6,'6x                  ',1595);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1002,120,16,1.6,'6x                  ',1399);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1003,166,24,2.5,'6x                  ',1899);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1004,166,32,2.5,'8x                  ',1999);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1005,166,16,2,'8x                  ',1999);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1006,200,32,3.1,'8x                  ',2099);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1007,200,32,3.2,'8x                  ',2349);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1008,180,32,2,'8x                  ',3699);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1009,200,32,2.5,'8x                  ',2599);
Insert into DBSTUDY.PC (MODEL,SPEED,RAM,HD,CD,PRICE) values (1010,160,16,1.2,'8x                  ',1495);
--------------------------------------------------------
--  DDL for Index SYS_C007377
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBSTUDY"."SYS_C007377" ON "DBSTUDY"."PC" ("MODEL") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
--------------------------------------------------------
--  Constraints for Table PC
--------------------------------------------------------

  ALTER TABLE "DBSTUDY"."PC" ADD PRIMARY KEY ("MODEL")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM"  ENABLE;
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("PRICE" NOT NULL ENABLE);
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("CD" NOT NULL ENABLE);
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("HD" NOT NULL ENABLE);
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("RAM" NOT NULL ENABLE);
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("SPEED" NOT NULL ENABLE);
  ALTER TABLE "DBSTUDY"."PC" MODIFY ("MODEL" NOT NULL ENABLE);
