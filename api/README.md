# Put The Spoon - Flask API Rest

### Como rodar o projeto:

O projeto foi desenvolvido usando a versão `3.6.5` do Python.

1. Antes de rodar o projeto é necessario subir o [banco do projeto](https://drive.google.com/file/d/1BJnbRitA4UF1svHUUz2Gv0jsIAYkYhlR/view?usp=sharing) no MySQl, execute o comando:

```
mysql -u root putthespoon_dev < backup_db.sql
```

Se você prefere utilizar o `MySQL Workbench`, relize os seguintes passos conectado no MySQL:

1.1. Selecione a opção `Data Import` e `Import from Disk`

1.2. Escolha a opção `Import from Self-Contained File`

1.3. Na opção `Schema to be Imported To` clique no botão `New` e coloque o nome do schema como `putthespoon_dev`

1.4. Clique em `Start Import`

1.5. Aguarde a operação ser finalizada

2. Instalar as dependencias:

```
pip install -r requirements.txt
```

3. Execute o comando para rodar o projeto:

```
flask run --host=0.0.0.0
```

### Dependencias para Linux

Se você utiliza Linux, é necessario instalar as seguintes dependencias para a aplicação conseguir [conectar com o banco MySQL](https://stackoverflow.com/a/23978968):

```
sudo apt install python3-dev
sudo apt install libmysqlclient-dev
```
