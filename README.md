# org-assets-trial

AI 組織の運用資産（org-assets）を Paperclip 上で試すための使い捨てリポジトリ。

## 開発規約

- テスト: `python -m pytest`
- Lint / 型チェック: なし
- 作業ブランチ: `feature/<task-id>` または `fix/<task-id>`。main への直接 push はブランチ保護で拒否される
- PR: `gh pr create` で作成し、概要に対応したタスク id・変更内容・テスト結果を書く
- コミットメッセージ: Conventional Commits、説明は日本語
