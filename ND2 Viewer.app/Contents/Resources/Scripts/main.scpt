FasdUAS 1.101.10   ��   ��    k             l     ��  ��    &   ND2 Viewer Launcher AppleScript     � 	 	 @   N D 2   V i e w e r   L a u n c h e r   A p p l e S c r i p t   
  
 l     ��  ��    , & Simplified version to prevent hanging     �   L   S i m p l i f i e d   v e r s i o n   t o   p r e v e n t   h a n g i n g      l     ��������  ��  ��     ��  i         I     ������
�� .aevtoappnull  �   � ****��  ��    Q    �     k   4       l   ��  ��    @ : Show immediate notification to confirm the app is running     �   t   S h o w   i m m e d i a t e   n o t i f i c a t i o n   t o   c o n f i r m   t h e   a p p   i s   r u n n i n g      I   ��   
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
psxp > o    ���� 0 apppath appPath < o      ���� 0 appposixpath appPosixPath :  ? @ ? l   ��������  ��  ��   @  A B A l   �� C D��   C E ? Remove "/ND2 Viewer.app" from the end to get project directory    D � E E ~   R e m o v e   " / N D 2   V i e w e r . a p p "   f r o m   t h e   e n d   t o   g e t   p r o j e c t   d i r e c t o r y B  F G F r    ( H I H l   & J���� J I   &�� K��
�� .sysoexecTEXT���     TEXT K b    " L M L m     N N � O O  d i r n a m e   M n    ! P Q P 1    !��
�� 
strq Q o    ���� 0 appposixpath appPosixPath��  ��  ��   I o      ���� $0 projectdirectory projectDirectory G  R S R l  ) )��������  ��  ��   S  T U T l  ) )�� V W��   V   Define paths    W � X X    D e f i n e   p a t h s U  Y Z Y r   ) 0 [ \ [ m   ) , ] ] � ^ ^ � / U s e r s / m i u r a / . p y e n v / v e r s i o n s / 3 . 1 1 . 5 / e n v s / L a t e s t S t a b l e / b i n / p y t h o n \ o      ���� 0 
pythonpath 
pythonPath Z  _ ` _ r   1 : a b a b   1 6 c d c o   1 2���� $0 projectdirectory projectDirectory d m   2 5 e e � f f 2 / w e b _ n d 2 _ v i e w e r _ s i m p l e . p y b o      ���� 0 
scriptpath 
scriptPath `  g h g l  ; ;��������  ��  ��   h  i j i l  ; ;�� k l��   k ) # Show what we found (for debugging)    l � m m F   S h o w   w h a t   w e   f o u n d   ( f o r   d e b u g g i n g ) j  n o n I  ; H�� p q
�� .sysonotfnull��� ��� TEXT p b   ; @ r s r m   ; > t t � u u  P r o j e c t :   s o   > ?���� $0 projectdirectory projectDirectory q �� v��
�� 
appr v m   A D w w � x x   N D 2   V i e w e r   D e b u g��   o  y z y l  I I��������  ��  ��   z  { | { l  I I�� } ~��   } 0 * Quick file existence check (non-blocking)    ~ �   T   Q u i c k   f i l e   e x i s t e n c e   c h e c k   ( n o n - b l o c k i n g ) |  � � � Q   I � � � � � I  L c�� ���
�� .sysoexecTEXT���     TEXT � b   L _ � � � b   L Y � � � b   L U � � � m   L O � � � � �  t e s t   - f   � n   O T � � � 1   R T��
�� 
strq � o   O R���� 0 
pythonpath 
pythonPath � m   U X � � � � �    & &   t e s t   - f   � n   Y ^ � � � 1   \ ^��
�� 
strq � o   Y \���� 0 
scriptpath 
scriptPath��   � R      ������
�� .ascrerr ****      � ****��  ��   � k   k � � �  � � � I  k ��� � �
�� .sysodlogaskr        TEXT � b   k � � � � b   k � � � � b   k � � � � b   k � � � � b   k � � � � b   k � � � � b   k ~ � � � b   k z � � � b   k v � � � b   k r � � � m   k n � � � � � 6 C a n n o t   f i n d   r e q u i r e d   f i l e s : � o   n q��
�� 
ret  � o   r u��
�� 
ret  � l 	 v y ����� � m   v y � � � � �  P y t h o n :  ��  ��   � o   z }���� 0 
pythonpath 
pythonPath � o   ~ ���
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
appr � m   � � � � � � �  N D 2   V i e w e r��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � 7 1 Launch server in background (simplified command)    � � � � b   L a u n c h   s e r v e r   i n   b a c k g r o u n d   ( s i m p l i f i e d   c o m m a n d ) �  � � � r   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � b   � � � � � m   � � � � � � �  c d   � n   � � � � � 1   � ���
�� 
strq � o   � ����� $0 projectdirectory projectDirectory � m   � � � � �      & &   � n   � � l 	 � ����� 1   � ���
�� 
strq��  ��   o   � ����� 0 
pythonpath 
pythonPath � m   � � �    � n   � � 1   � ���
�� 
strq o   � ����� 0 
scriptpath 
scriptPath � m   � � �		 8   >   / t m p / n d 2 v i e w e r . l o g   2 > & 1   & � o      ���� 0 	launchcmd 	launchCmd � 

 l  � ���������  ��  ��    I  �����
�� .sysoexecTEXT���     TEXT o   � ����� 0 	launchcmd 	launchCmd��    l �������  ��  �    l �~�~   ( " Wait a moment for server to start    � D   W a i t   a   m o m e n t   f o r   s e r v e r   t o   s t a r t  I �}�|
�} .sysodelanull��� ��� nmbr m  �{�{ �|    l 		�z�y�x�z  �y  �x    l 		�w�w     Open browser    �    O p e n   b r o w s e r  !  I 	�v"#
�v .sysonotfnull��� ��� TEXT" m  	$$ �%% $ O p e n i n g   b r o w s e r . . .# �u&�t
�u 
appr& m  '' �((  N D 2   V i e w e r�t  ! )*) I �s+�r
�s .sysoexecTEXT���     TEXT+ m  ,, �-- 8 o p e n   ' h t t p : / / 1 2 7 . 0 . 0 . 1 : 5 0 0 1 '�r  * ./. l �q�p�o�q  �p  �o  / 010 l �n23�n  2 !  Final success notification   3 �44 6   F i n a l   s u c c e s s   n o t i f i c a t i o n1 565 I "�m7�l
�m .sysodelanull��� ��� nmbr7 m  �k�k �l  6 898 I #2�j:;
�j .sysonotfnull��� ��� TEXT: m  #&<< �== J N D 2   V i e w e r   r e a d y !   C h e c k   y o u r   b r o w s e r .; �i>?
�i 
appr> m  '*@@ �AA  N D 2   V i e w e r? �hB�g
�h 
nsouB m  +.CC �DD  H e r o�g  9 E�fE l 33�e�d�c�e  �d  �c  �f    R      �bF�a
�b .ascrerr ****      � ****F o      �`�` 0 errormsg errorMsg�a    k  <�GG HIH l <<�_JK�_  J !  Show any error that occurs   K �LL 6   S h o w   a n y   e r r o r   t h a t   o c c u r sI MNM I <M�^OP
�^ .sysonotfnull��� ��� TEXTO b  <AQRQ m  <?SS �TT  E r r o r :  R o  ?@�]�] 0 errormsg errorMsgP �\UV
�\ 
apprU m  BEWW �XX   N D 2   V i e w e r   E r r o rV �[Y�Z
�[ 
nsouY m  FIZZ �[[ 
 B a s s o�Z  N \]\ l NN�Y�X�W�Y  �X  �W  ] ^�V^ I N��U_`
�U .sysodlogaskr        TEXT_ b  Noaba b  Ngcdc b  Ncefe b  N_ghg b  N[iji b  NYklk b  NUmnm m  NQoo �pp " N D 2   V i e w e r   E r r o r :n o  QT�T
�T 
ret l o  UX�S
�S 
ret j l 	YZq�R�Qq o  YZ�P�P 0 errormsg errorMsg�R  �Q  h o  [^�O
�O 
ret f o  _b�N
�N 
ret d l 	cfr�M�Lr m  cfss �tt  A p p   P a t h :  �M  �L  b l gnu�K�Ju n  gnvwv 1  ln�I
�I 
psxpw l glx�H�Gx I gl�Fy�E
�F .earsffdralis        afdry  f  gh�E  �H  �G  �K  �J  ` �Dz{
�D 
btnsz J  rw|| }�C} m  ru~~ �  O K�C  { �B��
�B 
dflt� m  z}�� ���  O K� �A��@
�A 
disp� m  ���?
�? stic    �@  �V  ��       �>���>  � �=
�= .aevtoappnull  �   � ****� �< �;�:���9
�< .aevtoappnull  �   � ****�;  �:  � �8�8 0 errormsg errorMsg� > !�7 %�6 (�5�4�3�2�1�0�/ N�.�-�, ]�+ e�* t w � ��)�( ��' � � ��& ��% ��$�#�"�! � � � � �� �$',<@C�SWZos~�
�7 
appr
�6 
nsou�5 
�4 .sysonotfnull��� ��� TEXT
�3 .earsffdralis        afdr
�2 
TEXT�1 0 apppath appPath
�0 
psxp�/ 0 appposixpath appPosixPath
�. 
strq
�- .sysoexecTEXT���     TEXT�, $0 projectdirectory projectDirectory�+ 0 
pythonpath 
pythonPath�* 0 
scriptpath 
scriptPath�)  �(  
�' 
ret 
�& 
btns
�% 
dflt
�$ 
disp
�# stic    �" 
�! .sysodlogaskr        TEXT�  0 	launchcmd 	launchCmd
� .sysodelanull��� ��� nmbr� 0 errormsg errorMsg�9�6������ O)j �&E�O��,E�O���,%j E�Oa E` O�a %E` Oa �%�a l O a _ �,%a %_ �,%j W OX  a _ %_ %a %_ %_ %a %_ %_ %_ %a %a a  kva !a "a #a $a % &OhO mna 'j oW X  hOa (�a )l Oa *��,%a +%_ �,%a ,%_ �,%a -%E` .O_ .j Omj /Oa 0�a 1l Oa 2j Okj /Oa 3�a 4�a 5� OPW TX 6 a 7�%�a 8�a 9� Oa :_ %_ %�%_ %_ %a ;%)j �,%a a <kva !a =a #a $a % &ascr  ��ޭ