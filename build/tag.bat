@setlocal
@echo off

if "%CD%\" NEQ "%~dp0" (
    echo Change working directory to [%~dp0]
    cd /d "%~dp0"
)
echo cwd: %CD%

set PROJECT_HOME=..\
set PACK_INPUT_DIR=%PROJECT_HOME%build\dest\
set PACK_OUTPUT_DIR=%PROJECT_HOME%packs\
set pack_file=tt_dims1_datapack.zip
set pack_filename_noext=tt_dims1_datapack
set pack_file_ext=.zip
set tag=%2

if /I "%~1" NEQ "" (
    set pack_file=%1
    set pack_filename_noext=%~n1
    set pack_file_ext=%~x1
)

if /I "%pack_file%" EQU "" (
    echo No pack_file indicated on argument 1.
    exit /b 1
)

if /I "%tag%" EQU "" (
    echo No tag indicated on argument 2.
    exit /b 2
)

set pack_output_file=%pack_filename_noext%-%tag%%pack_file_ext%

@rem --- request confirm ---

echo PACK_INPUT_DIR=%PACK_INPUT_DIR%
echo PACK_OUTPUT_DIR=%PACK_OUTPUT_DIR%
echo pack_file=%pack_file%
echo tag=%tag%
echo pack_output_file=%pack_output_file%

if not exist "%PACK_OUTPUT_DIR%%pack_output_file%" (
    choice /M "Confirm"
    if ERRORLEVEL 2 (
        exit /b 3
    )
) else (
    choice /M "Target output file exists, confirm and overwrite"
    if ERRORLEVEL 2 (
        exit /b 4
    )
    del /F /Q "%PACK_OUTPUT_DIR%%pack_output_file%"
    if ERRORLEVEL 1 (
        exit /b 5
    )
    if exist "%PACK_OUTPUT_DIR%%pack_output_file%" (
        exit /b 5
    )
)

@rem --- main ---

copy /V "%PACK_INPUT_DIR%%pack_file%" "%PACK_OUTPUT_DIR%%pack_output_file%"
if ERRORLEVEL 1 (
    exit /b 6
)
if not exist "%PACK_OUTPUT_DIR%%pack_output_file%" (
    exit /b 6
)

endlocal
exit /b 0

@rem EXIT_VALUES
@rem 0: 一切正常。
@rem 1: 未指定输入的数据包文件。
@rem 2: 未指定Tag。
@rem 3: 取消打标签发布。
@rem 4: 目标文件存在，用户取消打标签发布。
@rem 5: 目标文件存在，但无法删除。
@rem 6: 打标签发布失败。
