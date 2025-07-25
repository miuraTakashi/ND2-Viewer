FasdUAS 1.101.10   ��   ��    k             l     ��  ��    &   ND2 Viewer Launcher AppleScript     � 	 	 @   N D 2   V i e w e r   L a u n c h e r   A p p l e S c r i p t   
  
 l     ��  ��    , & Simplified version to prevent hanging     �   L   S i m p l i f i e d   v e r s i o n   t o   p r e v e n t   h a n g i n g      l     ��������  ��  ��     ��  i         I     ������
�� .aevtoappnull  �   � ****��  ��    Q    �     k   J       l   ��  ��    @ : Show immediate notification to confirm the app is running     �   t   S h o w   i m m e d i a t e   n o t i f i c a t i o n   t o   c o n f i r m   t h e   a p p   i s   r u n n i n g      I   ��   
�� .sysonotfnull��� ��� TEXT  m     ! ! � " " , N D 2   V i e w e r   s t a r t i n g . . .   �� # $
�� 
appr # m     % % � & &  N D 2   V i e w e r $ �� '��
�� 
nsou ' m     ( ( � ) ) 
 G l a s s��     * + * l   ��������  ��  ��   +  , - , l   �� . /��   . I C Simple approach: get project directory by going up from app bundle    / � 0 0 �   S i m p l e   a p p r o a c h :   g e t   p r o j e c t   d i r e c t o r y   b y   g o i n g   u p   f r o m   a p p   b u n d l e -  1 2 1 r     3 4 3 c     5 6 5 l    7���� 7 I   �� 8��
�� .earsffdralis        afdr 8  f    ��  ��  ��   6 m    ��
�� 
TEXT 4 o      ���� 0 apppath appPath 2  9 : 9 r     ; < ; n     = > = 1    ��
�� 
psxp > o    ���� 0 apppath appPath < o      ���� 0 appposixpath appPosixPath :  ? @ ? l   ��������  ��  ��   @  A B A l   �� C D��   C I C Remove "/app/ND2 Viewer.app" from the end to get project directory    D � E E �   R e m o v e   " / a p p / N D 2   V i e w e r . a p p "   f r o m   t h e   e n d   t o   g e t   p r o j e c t   d i r e c t o r y B  F G F l   �� H I��   H ? 9 First remove the app name, then remove the app directory    I � J J r   F i r s t   r e m o v e   t h e   a p p   n a m e ,   t h e n   r e m o v e   t h e   a p p   d i r e c t o r y G  K L K r    ( M N M l   & O���� O I   &�� P��
�� .sysoexecTEXT���     TEXT P b    " Q R Q m     S S � T T  d i r n a m e   R n    ! U V U 1    !��
�� 
strq V o    ���� 0 appposixpath appPosixPath��  ��  ��   N o      ���� 0 appdirectory appDirectory L  W X W r   ) 8 Y Z Y l  ) 4 [���� [ I  ) 4�� \��
�� .sysoexecTEXT���     TEXT \ b   ) 0 ] ^ ] m   ) , _ _ � ` `  d i r n a m e   ^ n   , / a b a 1   - /��
�� 
strq b o   , -���� 0 appdirectory appDirectory��  ��  ��   Z o      ���� $0 projectdirectory projectDirectory X  c d c l  9 9��������  ��  ��   d  e f e l  9 9�� g h��   g   Define paths    h � i i    D e f i n e   p a t h s f  j k j r   9 @ l m l m   9 < n n � o o � / U s e r s / m i u r a / . p y e n v / v e r s i o n s / 3 . 1 1 . 5 / e n v s / L a t e s t S t a b l e / b i n / p y t h o n m o      ���� 0 
pythonpath 
pythonPath k  p q p r   A L r s r b   A H t u t o   A D���� $0 projectdirectory projectDirectory u m   D G v v � w w 2 / w e b _ n d 2 _ v i e w e r _ s i m p l e . p y s o      ���� 0 
scriptpath 
scriptPath q  x y x l  M M��������  ��  ��   y  z { z l  M M�� | }��   | ) # Show what we found (for debugging)    } � ~ ~ F   S h o w   w h a t   w e   f o u n d   ( f o r   d e b u g g i n g ) {   �  I  M \�� � �
�� .sysonotfnull��� ��� TEXT � b   M T � � � m   M P � � � � �  P r o j e c t :   � o   P S���� $0 projectdirectory projectDirectory � �� ���
�� 
appr � m   U X � � � � �   N D 2   V i e w e r   D e b u g��   �  � � � l  ] ]��������  ��  ��   �  � � � l  ] ]�� � ���   � 0 * Quick file existence check (non-blocking)    � � � � T   Q u i c k   f i l e   e x i s t e n c e   c h e c k   ( n o n - b l o c k i n g ) �  � � � Q   ] � � � � � I  ` w�� ���
�� .sysoexecTEXT���     TEXT � b   ` s � � � b   ` m � � � b   ` i � � � m   ` c � � � � �  t e s t   - f   � n   c h � � � 1   f h��
�� 
strq � o   c f���� 0 
pythonpath 
pythonPath � m   i l � � � � �    & &   t e s t   - f   � n   m r � � � 1   p r��
�� 
strq � o   m p���� 0 
scriptpath 
scriptPath��   � R      ������
�� .ascrerr ****      � ****��  ��   � k    � � �  � � � I   ��� � �
�� .sysodlogaskr        TEXT � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � b    � � � � m    � � � � � � 6 C a n n o t   f i n d   r e q u i r e d   f i l e s : � o   � ���
�� 
ret  � o   � ���
�� 
ret  � l 	 � � ����� � m   � � � � � � �  P y t h o n :  ��  ��   � o   � ����� 0 
pythonpath 
pythonPath � o   � ���
�� 
ret  � l 	 � � ����� � m   � � � � � � �  S c r i p t :  ��  ��   � o   � ����� 0 
scriptpath 
scriptPath � o   � ���
�� 
ret  � o   � ���
�� 
ret  � l 	 � � ����� � m   � � � � � � � > P l e a s e   c h e c k   y o u r   i n s t a l l a t i o n .��  ��   � �� � �
�� 
btns � J   � � � �  ��� � m   � � � � � � �  O K��   � �� � �
�� 
dflt � m   � � � � � � �  O K � �� ���
�� 
disp � m   � ���
�� stic    ��   �  ��� � L   � �����  ��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � / ) Kill any existing server (quick timeout)    � � � � R   K i l l   a n y   e x i s t i n g   s e r v e r   ( q u i c k   t i m e o u t ) �  � � � Q   � � � ��� � t   � � � � � I  � ��� ���
�� .sysoexecTEXT���     TEXT � m   � � � � � � � j p k i l l   - f   ' p y t h o n . * w e b _ n d 2 _ v i e w e r '   2 > / d e v / n u l l   | |   t r u e��   � m   � �����  � R      ������
�� .ascrerr ****      � ****��  ��  ��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � "  Show launching notification    � � � � 8   S h o w   l a u n c h i n g   n o t i f i c a t i o n �  � � � I  � ��� � �
�� .sysonotfnull��� ��� TEXT � m   � � � � � � � . L a u n c h i n g   w e b   s e r v e r . . . � �� ���
�� 
appr � m   � � � � � � �  N D 2   V i e w e r��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � 7 1 Launch server in background (simplified command)    � � � � b   L a u n c h   s e r v e r   i n   b a c k g r o u n d   ( s i m p l i f i e d   c o m m a n d ) �  � � � r   � � � � b   �   b   � b   � b   � � b   � �	 b   � �

 m   � � �  c d   n   � � 1   � ���
�� 
strq o   � ����� $0 projectdirectory projectDirectory	 m   � � �    & &   n   � � l 	 � ����� 1   � ���
�� 
strq��  ��   o   � ����� 0 
pythonpath 
pythonPath m   � �    n   1  ��
�� 
strq o  ���� 0 
scriptpath 
scriptPath m   � 8   >   / t m p / n d 2 v i e w e r . l o g   2 > & 1   & � o      ���� 0 	launchcmd 	launchCmd �  l ��~�}�  �~  �}    I �|�{
�| .sysoexecTEXT���     TEXT o  �z�z 0 	launchcmd 	launchCmd�{    !  l �y�x�w�y  �x  �w  ! "#" l �v$%�v  $ ( " Wait a moment for server to start   % �&& D   W a i t   a   m o m e n t   f o r   s e r v e r   t o   s t a r t# '(' I �u)�t
�u .sysodelanull��� ��� nmbr) m  �s�s �t  ( *+* l �r�q�p�r  �q  �p  + ,-, l �o./�o  .   Open browser   / �00    O p e n   b r o w s e r- 121 I *�n34
�n .sysonotfnull��� ��� TEXT3 m  "55 �66 $ O p e n i n g   b r o w s e r . . .4 �m7�l
�m 
appr7 m  #&88 �99  N D 2   V i e w e r�l  2 :;: I +2�k<�j
�k .sysoexecTEXT���     TEXT< m  +.== �>> 8 o p e n   ' h t t p : / / 1 2 7 . 0 . 0 . 1 : 5 0 0 1 '�j  ; ?@? l 33�i�h�g�i  �h  �g  @ ABA l 33�fCD�f  C !  Final success notification   D �EE 6   F i n a l   s u c c e s s   n o t i f i c a t i o nB FGF I 38�eH�d
�e .sysodelanull��� ��� nmbrH m  34�c�c �d  G IJI I 9H�bKL
�b .sysonotfnull��� ��� TEXTK m  9<MM �NN J N D 2   V i e w e r   r e a d y !   C h e c k   y o u r   b r o w s e r .L �aOP
�a 
apprO m  =@QQ �RR  N D 2   V i e w e rP �`S�_
�` 
nsouS m  ADTT �UU  H e r o�_  J V�^V l II�]�\�[�]  �\  �[  �^    R      �ZW�Y
�Z .ascrerr ****      � ****W o      �X�X 0 errormsg errorMsg�Y    k  R�XX YZY l RR�W[\�W  [ !  Show any error that occurs   \ �]] 6   S h o w   a n y   e r r o r   t h a t   o c c u r sZ ^_^ I Rc�V`a
�V .sysonotfnull��� ��� TEXT` b  RWbcb m  RUdd �ee  E r r o r :  c o  UV�U�U 0 errormsg errorMsga �Tfg
�T 
apprf m  X[hh �ii   N D 2   V i e w e r   E r r o rg �Sj�R
�S 
nsouj m  \_kk �ll 
 B a s s o�R  _ mnm l dd�Q�P�O�Q  �P  �O  n o�No I d��Mpq
�M .sysodlogaskr        TEXTp b  d�rsr b  d}tut b  dyvwv b  duxyx b  dqz{z b  do|}| b  dk~~ m  dg�� ��� " N D 2   V i e w e r   E r r o r : o  gj�L
�L 
ret } o  kn�K
�K 
ret { l 	op��J�I� o  op�H�H 0 errormsg errorMsg�J  �I  y o  qt�G
�G 
ret w o  ux�F
�F 
ret u l 	y|��E�D� m  y|�� ���  A p p   P a t h :  �E  �D  s l }���C�B� n  }���� 1  ���A
�A 
psxp� l }���@�?� I }��>��=
�> .earsffdralis        afdr�  f  }~�=  �@  �?  �C  �B  q �<��
�< 
btns� J  ���� ��;� m  ���� ���  O K�;  � �:��
�: 
dflt� m  ���� ���  O K� �9��8
�9 
disp� m  ���7
�7 stic    �8  �N  ��       �6���6  � �5
�5 .aevtoappnull  �   � ****� �4 �3�2���1
�4 .aevtoappnull  �   � ****�3  �2  � �0�0 0 errormsg errorMsg� @ !�/ %�. (�-�,�+�*�)�(�' S�&�%�$ _�# n�" v�! � � � �� � �� � � �� �� ����� � � ���58=MQT�dhk����
�/ 
appr
�. 
nsou�- 
�, .sysonotfnull��� ��� TEXT
�+ .earsffdralis        afdr
�* 
TEXT�) 0 apppath appPath
�( 
psxp�' 0 appposixpath appPosixPath
�& 
strq
�% .sysoexecTEXT���     TEXT�$ 0 appdirectory appDirectory�# $0 projectdirectory projectDirectory�" 0 
pythonpath 
pythonPath�! 0 
scriptpath 
scriptPath�   �  
� 
ret 
� 
btns
� 
dflt
� 
disp
� stic    � 
� .sysodlogaskr        TEXT� 0 	launchcmd 	launchCmd
� .sysodelanull��� ��� nmbr� 0 errormsg errorMsg�1�L������ O)j �&E�O��,E�O���,%j E�Oa ��,%j E` Oa E` O_ a %E` Oa _ %�a l O a _ �,%a %_ �,%j W OX  a _ %_ %a %_ %_ %a %_ %_ %_ %a  %a !a "kva #a $a %a &a ' (OhO mna )j oW X  hOa *�a +l Oa ,_ �,%a -%_ �,%a .%_ �,%a /%E` 0O_ 0j Omj 1Oa 2�a 3l Oa 4j Okj 1Oa 5�a 6�a 7� OPW TX 8 a 9�%�a :�a ;� Oa <_ %_ %�%_ %_ %a =%)j �,%a !a >kva #a ?a %a &a ' (ascr  ��ޭ