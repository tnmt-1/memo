Pipenv
======

   PipenvはPythonのvirtualenv管理ツールで、多数のシステムをサポートし、pip、python（system
   python、pyenv、asdfを使用）、virtualenv間のギャップをうまく埋めている。Linux、macOS、Windowsはすべてpipenvの一級市民です。

   Pipenvは自動的にプロジェクト用のvirtualenvを作成・管理し、パッケージのインストール・アンインストールに合わせてPipfileからパッケージを追加・削除します。また、プロジェクトの
   Pipfile.lock を生成し、決定論的なビルドを行うために使用します。

URL
---

https://pipenv.pypa.io/en/latest/

Installation
------------

.. code:: shell

   pip install --user pipenv

Usage
-----

パッケージをインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   pipenv install requests

パッケージをアンインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   pipenv uninstall requests

virtualenv 内にシェルを起動する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   # 初回はバージョンすることが多い
   pipenv shell --python 3.12

   # 2回目以降はオプションを省略する
   pipenv shell

requirements.txt を生成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   pipenv requirements > requirements.txt

Pipfile.lock で指定されたすべてのパッケージをインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   pipenv sync --dev

Uninstallation
--------------

.. code:: shell

   pip uninstall --user pipenv
