@REM 将template.md复制到_posts目录下，并重命名为当前日期(yyyy-mm-dd) + title.md 的格式，title为第一个参数

@echo off
setlocal enabledelayedexpansion
 
set title=%1
set title=!title: =-!

REM 获取当前日期
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a

REM 提取年、月、日
set year=!datetime:~0,4!
set month=!datetime:~4,2!
set day=!datetime:~6,2!

REM 输出格式化后的日期
set date=%year%-%month%-%day%

set filename=%date%-%title%.md

copy template.md _posts\%filename%

@REM Path: template.md