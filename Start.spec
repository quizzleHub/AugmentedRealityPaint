# -*- mode: python ; coding: utf-8 -*-

############################################################################################
# This File is system dependent (The specified paths for the icons) 			           #
############################################################################################


block_cipher = None


a = Analysis(['src/Start.py'],
             pathex=[],
             binaries=[],
             datas=[('/home/user/Projekte/PyCharmProjects/AugmentedRealityPaint/icons_win/*.PNG', 'icons_win'),
             ('/home/user/Projekte/PyCharmProjects/AugmentedRealityPaint/icons_mac/*.PNG', 'icons_mac')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
