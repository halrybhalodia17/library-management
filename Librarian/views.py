from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LibrarianDb, Books, IssueReturn
from student.models import StudentDb
from .forms import Libform, Studinfo, AddBook, Removeform, Searchform, Issue, Returnform
import datetime
# Create your views here.
def login(request):
    if request.method == 'POST':
        userform = Libform(request.POST)
        ip_email = userform.data['email']
        ip_password = userform.data['password']
        try:
            lib = LibrarianDb.objects.get(email=ip_email)
            if lib.password == ip_password:
                context = {
                    "name":lib.name
                }
                return render(request,'librarian_dashboard.html',context)
            else:
                return  redirect('/librarian/error')
        except:
            return  redirect('/librarian/error')

    else:
        myform = Libform()
        return render(request, 'Librarian_login.html', {'form': myform})

def dashboard(request):
    
    return render(request,'librarian_dashboard.html')

def error(request):
    return render(request,'error.html')

def add_stud(request):
    try:
        if request.method == 'POST':
            studinfo = Studinfo(request.POST)
            ip_name = studinfo.data['name']
            ip_enroll = studinfo.data['enroll_no']
            ip_email = studinfo.data['email']
            ip_branch = studinfo.data['branch']
            ip_phone = studinfo.data['phone_no']
            ip_password = studinfo.data['password']
            ip_roll = studinfo.data['roll_no']
            ip_shift = studinfo.data['shift']
            stud = StudentDb(enroll_no=ip_enroll, name=ip_name, email=ip_email,branch=ip_branch, phone_no=ip_phone, password=ip_password, roll_no=ip_roll, shift=ip_shift)
            stud.save()
            msg = "Student Added Successfully"
        else:
            msg=""
    except:
        msg = "Enrollment number or Email already exist"
    
    context={
        'msg':msg
    }
    
    return render(request,'add_stud.html',context)

def add_book(request):
    try:
        if request.method == 'POST':
            add_book = AddBook(request.POST)
            ip_name = add_book.data['name']
            ip_author = add_book.data['author']
            ip_total = add_book.data['total']
            book = Books(name=ip_name, author=ip_author, total=ip_total)
            book.save()
            msg = "Book Added Successfully"
        else:
            msg = ""
    except:
        if request.method == 'POST':
            add_book= AddBook(request.POST)
            ip_name = add_book.data['name']
            ip_author = add_book.data['author']
            ip_total = add_book.data['total']
            updatebook= Books.objects.get(name=ip_name)

            if updatebook.author == ip_author:
                add = updatebook.total + int(ip_total)
                updatebook.total = add
                updatebook.save()
                msg = "Book quantity added"
        else:
            msg = ""
   
    
    context={
        'msg':msg
    }

    print(msg)
    return render(request,'add_book.html', context)

def remove_book(request):
    books = Books.objects.all()
    book_nid=[]
    for i in range(len(books)):
        book_nid.append([books[i].name.lower(),books[i].author,books[i].id])
    
    book_nid.sort()

    if request.method == 'POST':
        removebook = Removeform(request.POST)
        ip_bid = removebook.data['bid']
        remove = Books.objects.get(id = ip_bid)
        remove.delete()
        msg = "Book Removed"
    else:
        msg=""

    context ={
        'book_nid': book_nid,
        'msg':msg
    }

    return render(request,'remove_book.html',context)

def search(request):
    books = Books.objects.all()
    book_nid=[]
    for i in range(len(books)):
        book_nid.append([books[i].name.lower(),books[i].author,books[i].id])
    
    if request.method == 'POST':
        searchbook = Searchform(request.POST)
        ip_bid = searchbook.data['bid']
        search = Books.objects.get(id = ip_bid)
        total = search.total
        msg = "Available:"
    else:
        total =""
        msg=""

    context ={
        'book_nid': book_nid,
        'msg':msg,
        'total':total
    }
    
    book_nid.sort()
    return render(request,'Search.html',context)

def issue_return(request):
    student = StudentDb.objects.all()
    email=[]
    for i in range(len(student)):
        email.append(student[i].email)
    email.sort()

    books = Books.objects.all()
    book_nid=[]
    for i in range(len(books)):
        book_nid.append([books[i].id,books[i].name.lower()])
    
    book_nid = sorted(book_nid, key = lambda x: x[1])

    if request.method == 'POST':
        issue = Issue(request.POST)
        ip_email = issue.data['semail']
        ip_bookid = issue.data['bname']

        student = StudentDb.objects.get(email = ip_email)
        book = Books.objects.get(id =ip_bookid)
        ip_total = book.total

        if ip_total>0:
            ip_bookname = book.name
            book.total = book.total -1 
            book.save()
            issue_date = datetime.datetime.now() 
            yy = issue_date.year
            mm = issue_date.month
            dd = issue_date.day
            issue = datetime.date(yy,mm,dd)
            return_date = datetime.date(2000,10,10)

            issue_book = IssueReturn(
                email=student, 
                book_id=book, 
                book_name=ip_bookname,
                issue_date=issue,
                return_date=return_date
            )
            issue_book.save()
            
            msg = "Book issued"
        else:
            msg = "Unavaiable Book"
    else:
        msg = ""
    context = {
        'email':email,
        'book_nid':book_nid,
        'msg':msg
    }

    return render(request,'issue_return.html', context)


def return_book(request):
    student = IssueReturn.objects.all()
    email=[]
    for i in range(len(student)):
        if student[i].email.email not in email:
            email.append(student[i].email.email)
    email.sort()
    
    if request.method == 'POST':
        issue = Returnform(request.POST)
        ip_email = issue.data['semail']
        return redirect('/librarian/return1/' + ip_email)


    context = {
        'email':email
    }

    return render(request,'return.html',context)

def return1(request, email):
    print(email)
    books = IssueReturn.objects.all()
    book_nid=[]
    for i in range(len(books)):
        if books[i].book_id.name.lower() not in book_nid:
            book_nid.append([books[i].book_id.name.lower(),books[i].book_id.author,books[i].book_id.id])
    book_nid.sort()

    context = {
        'book_nid':book_nid
    }

    return render(request,'return1.html',context)




