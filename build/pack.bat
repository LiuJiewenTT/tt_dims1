@ setlocal
@ echo off

if "%CD%\" NEQ "%~dp0" (
    echo Change working directory to [%~dp0]
    cd /d "%~dp0"
)
echo cwd: %CD%

set PROJECT_HOME=..\
set SRC_DIR=%PROJECT_HOME%src\
set DEST_DIR=%PROJECT_HOME%build\dest\
set pack_filename_noext=tt_dims2_datapack
set pack_file_ext=.zip
set pack_filename=%pack_filename_noext%%pack_file_ext%

if /I "%~1" NEQ "" (
    set pack_filename_noext=%1
)

@rem --- request confirm ---

echo SRC_DIR=%SRC_DIR%
echo DEST_DIR=%DEST_DIR%
echo pack_filename_noext=%pack_filename_noext%
choice /M "Confirm"
if ERRORLEVEL 2 (
    exit /b 1
)

@rem --- main ---

if not exist "%DEST_DIR%" (
    echo Create DEST_DIR
    mkdir "%DEST_DIR%"
)

if exist "%DEST_DIR%%pack_filename%" (
    echo Delete old package file [%DEST_DIR%%pack_filename%]
    del /F /Q "%DEST_DIR%%pack_filename%"
    if ERRORLEVEL 1 (
        exit /b 2
    )
)
if exist "%DEST_DIR%%pack_filename%" (
    exit /b 2
)

7z a -sse "%DEST_DIR%%pack_filename%" "%SRC_DIR%%pack_filename_noext%\*"
if ERRORLEVEL 1 (
    exit /b 3
)
if not exist "%DEST_DIR%%pack_filename%" (
    exit /b 3
)

endlocal
exit /b 0

@rem EXIT_VALUES
@rem 0: 一切正常。
@rem 1: 取消打包。
@rem 2: 无法删除旧数据包文件。
@rem 3: 打包失败。
