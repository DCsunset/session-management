use async_trait::async_trait;

#[async_trait]
pub trait TokenStore {
	async fn contains(&self, token: String) -> bool;
	async fn insert(&self, token: String);
}
