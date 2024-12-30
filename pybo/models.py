from sqlalchemy.orm import backref

from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model): #db.Model 클래스 상속
    id = db.Column(db.Integer, primary_key=True) #데이터 타입 Integer, 중복된 값을 가질 수 없도록 id에 기본 키 부여.
    subject = db.Column(db.String(200), nullable=False)  #글자 수 제한 200, Null 값 비허용
    content = db.Column(db.Text(), nullable=False) #글자 수 제한 X, 따라서 String이 아닌 Text 사용.
    create_date = db.Column(db.DateTime(), nullable=False) #날짜와 시각에 해당하는 DateTime 사용
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    #question 테이블의 id 컬럼(question.id)과 연결하기 위해 외부 키(ForeignKey) 사용. onedelte를 통해 질문 삭제시 답변도 함께 삭제.
    question = db.relationship('Question', backref=db.backref('answer_set'))
    #Qusetion을 참조하여 answer.question.subject처럼 제목 설정. backref로 역참조 하여 답변을 참조.
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
