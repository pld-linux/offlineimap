Summary:	Mailboxes synchronization tool
Summary(pl.UTF-8):	Narzędzie do synchroniczacji skrzynek pocztowych
Name:		offlineimap
Version:	5.99.14
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://software.complete.org/software/versions/download/235?attachment_id=313
# Source0-md5:	cac3fff4f1cc5cbd7acf5a544c13152c
URL:		http://software.complete.org/software/projects/show/offlineimap
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OfflineIMAP is a tool to simplify your e-mail reading. With
OfflineIMAP, you can read the same mailbox from multiple computers.
You get a current copy of your messages on each computer, and changes
you make one place will be visible on all other systems. For instance,
you can delete a message on your home computer, and it will appear
deleted on your work computer as well. OfflineIMAP is also useful if
you want to use a mail reader that does not have IMAP support, has
poor IMAP support, or does not provide disconnected operation.

%description -l pl.UTF-8
OfflineIMAP to narzędzie upraszczające czytanie poczty elektronicznej.
Za jego pomocą można czytać tą samą skrzynkę z wielu komputerów.
Pobiera się aktualną kopię wiadomości na każdym komputerze, a zmiany
dokonywane w jednym miejscu będą widoczne na wszystkich innych
systemach. Na przyklad, można usunąć wiadomość na swoim domowym
komputerze i zostanie ona usunięta także na komputerze w pracy.
OfflineIMAP jest przydatne także jeśli chcemy używać czytnika poczty
bez obsługi IMAP, z kiepską obsługą IMAP albo nie działającego bez
połączenia.

%prep
%setup -q -n %{name}
sed -i 's/env python2.3/python/' *.py

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ.html UPGRADING offlineimap.conf*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
