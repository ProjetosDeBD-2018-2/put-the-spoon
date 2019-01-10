# Put The Spoon - Flask API Rest

### Como rodar o projeto:

O projeto foi desenvolvido usando a versão `3.6.5` do Python.

1. Antes de rodar o projeto é necessario subir o [banco do projeto] no MySQl(https://drive.google.com/file/d/1BJnbRitA4UF1svHUUz2Gv0jsIAYkYhlR/view?usp=sharing), execute o comando:

```
mysql -u root putthespoon_dev < backup_db.sql
```

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
