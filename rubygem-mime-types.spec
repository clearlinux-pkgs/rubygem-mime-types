#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-mime-types
Version  : 2.6.1
Release  : 8
URL      : https://rubygems.org/downloads/mime-types-2.6.1.gem
Source0  : https://rubygems.org/downloads/mime-types-2.6.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-rdoc

%description
= mime-types
home :: https://github.com/mime-types/ruby-mime-types/
code :: https://github.com/mime-types/ruby-mime-types/
bugs :: https://github.com/mime-types/ruby-mime-types/issues
rdoc :: http://rdoc.info/gems/mime-types/
continuous integration :: {<img src="https://travis-ci.org/mime-types/ruby-mime-types.png" />}[https://travis-ci.org/mime-types/ruby-mime-types]
test coverage :: {<img src="https://coveralls.io/repos/mime-types/ruby-mime-types/badge.png" alt="Coverage Status" />}[https://coveralls.io/r/mime-types/ruby-mime-types]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n mime-types-2.6.1
gem spec %{SOURCE0} -l --ruby > rubygem-mime-types.gemspec

%build
gem build rubygem-mime-types.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
mime-types-2.6.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/mime-types-2.6.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/.hoerc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/Contributing.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/History-Types.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/History.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/Licence.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime-types.json
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.content_type.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.docs.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.encoding.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.friendly.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.obsolete.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.references.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.registered.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.signature.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.system.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.use_instead.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/data/mime.xrefs.column
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/docs/COPYING.txt
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/docs/artistic.txt
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime-types.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/type.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/type/columnar.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/columnar.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/deprecations.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/loader.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/loader_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/lib/mime/types/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/apache_mime_types.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/benchmarks/load.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/benchmarks/load_allocations.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/benchmarks/object_counts.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/convert.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/convert/columnar.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/support/iana_registry.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/bad-fixtures/malformed
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/fixture/json.json
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/fixture/old-data
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/fixture/yaml.yaml
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/minitest_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_type.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_types.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_types_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_types_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_types_lazy.rb
/usr/lib64/ruby/gems/2.3.0/gems/mime-types-2.6.1/test/test_mime_types_loader.rb
/usr/lib64/ruby/gems/2.3.0/specifications/mime-types-2.6.1.gemspec
