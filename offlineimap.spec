Summary:	Mailboxes synchronization tool
Summary(pl):	Narzêdzie do synchroniczacji skrzynek pocztowych
Name:		offlineimap
Version:	4.0.12
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://gopher.quux.org:70/devel/offlineimap/%{name}_%{version}.tar.gz
# Source0-md5:	aa2b67d3462cb1011f4577d7121eb72c
URL:		gopher://gopher.quux.org/1/devel/offlineimap
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

%description -l pl
OfflineIMAP to narzêdzie upraszczaj±ce czytanie poczty elektronicznej.
Za jego pomoc± mo¿na czytaæ t± sam± skrzynkê z wielu komputerów.
Pobiera siê aktualn± kopiê wiadomo¶ci na ka¿dym komputerze, a zmiany
dokonywane w jednym miejscu bêd± widoczne na wszystkich innych
systemach. Na przyklad, mo¿na usun±æ wiadomo¶æ na swoim domowym
komputerze i zostanie ona usuniêta tak¿e na komputerze w pracy.
OfflineIMAP jest przydatne tak¿e je¶li chcemy u¿ywaæ czytnika poczty
bez obs³ugi IMAP, z kiepsk± obs³ug± IMAP albo nie dzia³aj±cego bez
po³±czenia.

%prep
%setup -q -n %{name}
sed -i 's/env python2.3/python/' *.py

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README offlineimap.conf*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_mandir}/man1/*
