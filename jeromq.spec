%{?scl:%scl_package jeromq}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jeromq
Version:	0.3.6
Release:	3%{?dist}
Summary:	Pure Java implementation of libzmq
License:	MPLv2.0
URL:		https://github.com/zeromq/jeromq
BuildArch:	noarch

Source0:	https://github.com/zeromq/%{pkg_name}/archive/v%{version}.tar.gz#/%{pkg_name}-%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}maven-plugin-bundle
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
%{?scl:Requires: %scl_runtime}

%description
Pure Java implementation of libzmq.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-source-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Tests require network access and fail on Koji.
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md CHANGELOG.md AUTHORS
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Mar 01 2017 Tomas Repik <trepik@redhat.com> - 0.3.6-3
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.6-1
- Update to upstream version 0.3.6

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.5-5
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.5-3
- Skip running checkstyle during build

* Mon Oct  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.5-2
- Skip running tests
- Add comment clarify licensing

* Wed Aug 26 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.5-1
- Initial packaging
