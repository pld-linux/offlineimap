%bcond_without	doc
#
Summary:	Mailboxes synchronization tool
Summary(pl.UTF-8):	Narzędzie do synchroniczacji skrzynek pocztowych
Name:		offlineimap
Version:	6.5.6
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://github.com/OfflineIMAP/%{name}/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	b595561eb2050767c376df3b92aa0d74
Patch0:		%{name}-docs.patch
URL:		https://offlineimap.org
BuildRequires:	rpm-pythonprov >= 4.1-13
%if %{with doc}
BuildRequires:	docutils
BuildRequires:	sphinx-pdg
%endif
Suggests:	python-sqlite
BuildArch:	noarch
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
%setup -q
%patch0 -p1

%build
%if %{with doc}
%{__make} doc
%{__make} man
%endif

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
install %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%if %{with doc}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc offlineimap.conf*
%if %{with doc}
%doc Changelog.html README.md docs/html/*.html
%{_mandir}/man1/offlineimap.1*
%endif
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
