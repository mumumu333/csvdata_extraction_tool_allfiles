���c�[���T�v��
run.bat�Ō����l���w��B�����l���܂܂��csv�t�@�C������肵�Aresult.txt�ɏo�͂���B

���C���X�g�[���ҁ�
�@��Python �C���X�g�[��
�@�@https://www.python.org/downloads/
�@�@
�@�@2023/4/21 ���_�̍ŐV����F3.11.3 ���g�p

�@��VisualStudioCode �C���X�g�[��
�@�@https://code.visualstudio.com/Download
�@�@
�@�@2023/4/21 ���_�̍ŐV����F1.77.3 ���g�p

�����O�����ҁ�
�@�@���z���쐬
�@�@�Q�lURL�Fhttps://qiita.com/nosniklim/items/1d4c480e3accd3eb8c0f
�@�@
�@�@�E���z���쐬
�@�@�@py -m venv csvdata_extraction_tool_allfiles
�@
�@�@�E���z����L���ɂ���
�@�@�@cd csvdata_extraction_tool_allfiles
�@�@�@Scripts\activate

�@�A���C�u�����̃C���X�g�[��
�@�@�Epip�̍ŐV���i���C�u�����C���X�g�[���p�R�}���h���ŐV�ɂ���j
�@�@�@python -m pip install

�@�@�Epandas�̃C���X�g�[���i�G�N�Z������̃��C�u�����j
�@�@�@pip install pandas

�@�Bcsvdata_extraction_tool_allfiles.py���@�ō쐬�������z���z���Ɏ����Ă���

�@�Crun.bat�t�@�C���̒��g��ҏW�B���L�̈����Ŏ��s����邽�ߒ��o�������f�[�^�ɉ����ĕύX����
�@�@py csvdata_extraction_tool_allfiles.py �����Ώ�CSV�t�@�C���̐e�f�B���N�g���@ �����l�@>> result.txt

�@�@(��.)137�A459�ABrandon�AJack�̒P����܂ރt�@�C���𒊏o�������ꍇ
�@�@�@�@set file_path="C:\Users\~\csvdata_extraction_tool_allfiles\testfolder"

�@�@�@�@py csvdata_extraction_tool_allfiles.py %file_path% 137 >> result.txt
�@�@�@�@py csvdata_extraction_tool_allfiles.py %file_path% 459 >> result.txt
�@�@�@�@py csvdata_extraction_tool_allfiles.py %file_path% Brandon >> result.txt
�@�@�@�@py csvdata_extraction_tool_allfiles.py %file_path% Jack >> result.txt

�@�D�R�}���h�v�����v�g�ɂ�run.bat�t�@�C�������s�B���ʂ�result.txt�ɏo�͂����B
�@�@run.bat

������F�R�}���h���C�����Ƃ����灄
�@�E���z����L���ɂ���
�@�@cd csvdata_extraction_tool_allfiles
�@�@Scripts\activate

��run.bat�t�@�C�����s���ɕ����������Ă���Ƃ��A�f�B���N�g���w��ŃG���[���o��ꍇ��
�@chcp 65001
�@����͂��čēx���s