Summary:	Mailboxes synchronization tool
Summary(pl):	Narz�dzie do synchroniczacji skrzynek pocztowych
Name:		offlineimap
Version:	4.0.11
Release:	0.1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://gopher.quux.org:70/devel/offlineimap/%{name}_%{version}.tar.gz
# Source0-md5:	41af0924d5e19480377616f4b1d059e1
URL:		gopher://gopher.quux.org/1/devel/offlineimap
#BuildRequires:	rpm-pythonprov >= 4.1-13
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

%description -l pl

%prep
%setup -q -n %{name}
sed -i 's/env python2.3/python/' *.py
%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README offlineimap.conf*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
