<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <widget name="__qt_fake_top_level">
  <widget class="QPlainTextEdit" name="PlainTextEdit">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>250</y>
     <width>255</width>
     <height>100</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="PlainFileLabel">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>220</y>
     <width>251</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Исходный файл:</string>
   </property>
  </widget>
  <widget class="QLabel" name="KeyLabel">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>90</y>
     <width>300</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Сгенерированный ключ:</string>
   </property>
  </widget>
  <widget class="QLabel" name="CipherFileLabel">
   <property name="geometry">
    <rect>
     <x>315</x>
     <y>220</y>
     <width>251</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Зашифрованный файл:</string>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="KeyEdit">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>120</y>
     <width>300</width>
     <height>75</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="CipherEditLabel">
   <property name="geometry">
    <rect>
     <x>315</x>
     <y>250</y>
     <width>255</width>
     <height>100</height>
    </rect>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="StartConditionEdit">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>55</y>
     <width>300</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>14</pointsize>
    </font>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>50</y>
     <width>200</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Зашифровать</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>90</y>
     <width>200</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Расшифровать</string>
   </property>
  </widget>
  <widget class="QLabel" name="StartConditionLabel">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>25</y>
     <width>350</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Введите начальное состояние регистра:</string>
   </property>
  </widget>
 </widget>
 <resources/>
</ui>
