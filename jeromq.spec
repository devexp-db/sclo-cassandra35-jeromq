Name:           jeromq
Version:        0.3.5
Release:        5%{?dist}
Summary:        Pure Java implementation of libzmq
# License headers in source files seem to indicate LGPLv3+, but pom.xml as well
# as upstream licensing page (http://zeromq.org/area:licensing) specify license
# as LGPLv3 only - lets use stricter variant as safer choice.
License:        LGPLv3
URL:            https://github.com/zeromq/jeromq
BuildArch:      noarch

Source0:        https://github.com/zeromq/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
Pure Java implementation of libzmq.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-checkstyle-plugin

%build
# Tests require network access and fail on Koji.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md CHANGELOG.md AUTHORS
%license COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%license COPYING.LESSER

%changelog
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
